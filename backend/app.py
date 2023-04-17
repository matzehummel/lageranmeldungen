from dotenv import load_dotenv
import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import smtplib, ssl
import jinja2
import pdfkit
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()

app = Flask(__name__)
CORS(app, resources = {r"/*": { "origins": "*" }})

mongodb_connection_string = os.environ.get('MONGODB_CONNECTION_STRING')
mongoClient = MongoClient(mongodb_connection_string)
db = mongoClient.lageranmeldungen
print("Connected to database")

@app.route('/index')
@cross_origin()
def index():
    return "POST /registration"

@app.route('/registration/kinderlager', methods=['POST'])
@cross_origin()
def add_registration():
    data = request.get_json()
    collection = db["registrations"]
    result = collection.insert_one(parseDataForDb(data, type="kinderlager"))
    data, pdfFilename, childFirstName, childLastName = parseData(data)
    send_mail_result = send_Mail(data, create_pdf(data, pdfFilename, "kinderlager"), childFirstName, childLastName, "kinderlager")
    print(send_mail_result)
    return 'New registration added to database: ' + str(result.inserted_id)

@app.route('/registration/xxl', methods=['POST'])
@cross_origin()
def add_registration_xxl():
    data = request.get_json()
    collection = db["registrations_xxl"]
    dbData = parseDataForDb(data, type="xxl")
    result = collection.insert_one(dbData)
    data, pdfFilename, childFirstName, childLastName = parseData(data)
    send_mail_result = send_Mail(data, create_pdf(data, pdfFilename, "xxl"), childFirstName, childLastName, "xxl")
    print(send_mail_result)
    return 'New registration added to database: ' + str(result.inserted_id)

def parseDataForDb(data, type):
    dbData = {}
    for item in data:
        dbData[item] = data[item].replace("ü", "ue")
        dbData[item] = dbData[item].replace("ö", "oe")
        dbData[item] = dbData[item].replace("ä", "ae")
        dbData[item] = dbData[item].replace("Ü", "Ue")
        dbData[item] = dbData[item].replace("Ö", "Oe")
        dbData[item] = dbData[item].replace("Ä", "Ae")
        dbData[item] = dbData[item].replace("ß", "ss")
        dbData[item] = dbData[item].replace("\n", " ")
        dbData[item] = dbData[item].replace("\r", " ")
        dbData[item] = dbData[item].replace(",", ";")

    if(type == "xxl"):
        dbData["experienceKinderlager"] = {
            "nie dabei": 0,
            "1 mal dabei": 1,
            "2 mal dabei": 2,
            "3 mal dabei": 3,
            "4 mal dabei": 4
        }.get(dbData["experienceKinderlager"], "undef")

        dbData["experienceXXL"] = {
            "noch nie dabei": 0,
            "1 mal dabei": 1,
            "2 mal dabei": 2
        }.get(dbData["experienceXXL"], "undef")
    
    elif(type == "kinderlager"):
        dbData["experience"] = {
            "schon einmal auf dem Zeltlager dabei": 1,
            "noch nie dabei": 0
        }.get(dbData["experience"], "undef")

    return dbData


def parseData(data):
    if(data["tetanus"] == "1"):
        data["tetanus"] = "bin ich geimpft"
    else:
        data["tetanus"] = "bin ich NICHT geimpft"

    if(data["swim"] == "1"):
        data["swim"] = "schwimmen"
    else:
        data["swim"] = "NICHT schwimmen"
    
    if(data["swimAllowed"] == "1"):
       data["swimAllowed"] = "erlaubt"
    else:
        data["swimAllowed"] = "NICHT erlaubt"

    if(data["milk"] == "1"):
        data["milk"] = "ungekochte, frische Milch trinken."
    else:
        data["milk"] = "KEINE ungekochte, frische Milch trinken."
    
    if(data["availability"] == "1"):
        data["availability"] = "unter obiger Anschrift zu erreichen."
    elif(data["availability"] == "2"):
        data["availability"] = "im Urlaub unter folgender Anschrift zu erreichen:"
    elif(data["availability"] == "3"):
        data["availability"] = "nicht zu erreichen, folgende Personen k&ouml;nnen als Kontaktpersonen angesprochen werden:"

    if(data["sonst"] == ""):
        data["sonst"] = "-"

    pdfFilename = "Anmeldebestaetigung_" + data["childFirstName"] + data["childLastName"] + ".pdf"
    childFirstName = data["childFirstName"]
    childLastName = data["childLastName"]
    pdfFilename = pdfFilename.replace("ü", "ue")
    pdfFilename = pdfFilename.replace("Ü", "Ue")
    pdfFilename = pdfFilename.replace("ä", "ae")
    pdfFilename = pdfFilename.replace("Ä", "Ae")
    pdfFilename = pdfFilename.replace("ö", "oe")
    pdfFilename = pdfFilename.replace("Ö", "Oe")
    pdfFilename = pdfFilename.replace("ß", "ss")

    for item in data:
        if not(item == "_id"):
            data[item] = str(data[item]).replace("ü", "&uuml;")
            data[item] = str(data[item]).replace("ö", "&ouml;")
            data[item] = str(data[item]).replace("ä", "&auml;")
            data[item] = str(data[item]).replace("Ü", "&Uuml;")
            data[item] = str(data[item]).replace("Ö", "&Ouml;")
            data[item] = str(data[item]).replace("Ä", "&Auml;")
            data[item] = str(data[item]).replace("ß", "&#223;")
            data[item] = str(data[item]).replace("\n", "<br>")
    return data, pdfFilename, childFirstName, childLastName

def create_pdf(data, pdfFilename, type):
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)
    
    #reads template and replaces the placeholder with the given JSON-Data
    if(type == "xxl"):
        template=template_env.get_template('html-template-xxl.html')
    elif(type == "kinderlager"):    
        template=template_env.get_template('html-template.html')
    output_text=template.render(data)
    #PDFfilename = "Anmeldebestaetigung_"+data["childFirstName"]+data["childLastName"]+".pdf"
    
    #set the location of wkhtmltopdf and it generates the pdf
    config  =pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_PATH'))
    options = {
        'page-size': 'A4',
        'margin-top': '2cm',
        'margin-right': '2cm',
        'margin-bottom': '2cm',
        'margin-left': '2cm'
    }

    pdfkit.from_string(output_text, 'pdf/'+pdfFilename, configuration=config, options=options)
    return pdfFilename

def send_Mail(data, PDFfilename, childFirstName, childLastName, type):
    #Variablen setzen
    smtp_server="mx2efc.netcup.net"
    mail_sender="anmeldung@zeltlager-braeunlingen.de"
    mail_receiver = data["email"]
    password = os.environ.get('EMAIL_PASSWORD')

    message=MIMEMultipart()
    #HTML-Mailbody erstellen und Variable message anhaengen
    if(type == "kinderlager"):
        htmlbody="""\
        <p>Hallo {},<br />
        <br />
        Hurra! Deine Anmeldung f&uuml;r das Zeltlager 2023 hat erfolgreich funktioniert.<br />
        Im Anhang findest du eine PDF-Datei mit all deinen angegebenen Daten.<br />
        Drucke die PDF bitte aus, <u><strong>lass deine Eltern darauf unterschreiben</strong></u> und bring es zum Vortreffen wieder mit.<br />
        Alternativ kannst du das unterschriebene Formular im Pfarrbüro oder bei einem Lagerleiter einwerfen.
        <br/><br/>
        Wir freuen uns schon auf ein wundersch&ouml;nes Zeltlager 2023 mit Dir!<br />
        Deine Leiterrunde</p>
        """.format(childFirstName)
        message["subject"] = "Zeltlager 2023 - Anmeldung von " + childFirstName + " " + childLastName
    elif(type == "xxl"):
        htmlbody="""\
        <p>Hallo {},<br />
        <br />
        Hurra! Deine Anmeldung f&uuml;r das XXL-Lager 2023 hat erfolgreich funktioniert.<br />
        Im Anhang findest du eine PDF-Datei mit all deinen angegebenen Daten.<br />
        Drucke die PDF bitte aus, <u><strong>lass deine Eltern darauf unterschreiben</strong></u> und bring es zum Vortreffen wieder mit.<br />
        Alternativ kannst du das unterschriebene Formular im Pfarrbüro oder bei Lagerleiter Christian in Döggingen einwerfen.
        <br/><br/>
        Wir freuen uns schon auf ein wundersch&ouml;nes XXL 2023 mit Dir!<br />
        Deine XXL-Leiterrunde</p>
        """.format(childFirstName)
        message["subject"] = "XXL 2023 - Anmeldung von " + childFirstName + " " + childLastName
   
    
    message["From"]=mail_sender
    message["To"]=mail_receiver
    messagebody=MIMEText(htmlbody, "html")
    message.attach(messagebody)

    #Mail-Attachment anhaengen
    with open("pdf/"+PDFfilename,"rb")as attachment:
        pdf = MIMEBase("application/pdf","octet-stream")
        pdf.set_payload(attachment.read())
    encoders.encode_base64(pdf)
    pdf.add_header(
        "Content-Disposition",
        "attachment", filename= PDFfilename
    )
    message.attach(pdf)

    #Am Mail-Server authentifizieren und Mail senden
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server,port=465,context=context) as server:
        try:
            server.login(mail_sender,password)
        except:
            return 'authentication on mail server failed'
        try:
            server.sendmail(mail_sender, mail_receiver, message.as_string())
            server.sendmail(mail_sender, mail_sender, message.as_string())
        except:
            return 'mail was not sent, but authentication was successful'
    return 'Mail Sent!'

if __name__ == '__main__':
    app.run(debug=True)
