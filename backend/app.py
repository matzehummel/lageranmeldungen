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
CORS(app, origins="*")

mongodb_connection_string = os.environ.get('MONGODB_CONNECTION_STRING')
mongoClient = MongoClient(mongodb_connection_string)
db = mongoClient.lageranmeldungen
print("Connected to database")

@app.route('/registration', methods=['POST'])
@cross_origin()
def add_registration():
    data = request.get_json()
    collection = db["registrations"]
    result = collection.insert_one(data)
    data, pdfFilename = parseData(data)
    print(send_Mail(data, create_pdf(data, pdfFilename)))
    return 'New registration added to database: ' + str(result.inserted_id)

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

    pdfFilename = "Anmeldebestaetigung_" + data["childFirstName"] + data["childLastName"] + ".pdf"
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
            data[item] = str(data[item]).replace("ß", "&#223;")
    return data, pdfFilename

def create_pdf(data, pdfFilename):
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)
    
    #reads template and replaces the placeholder with the given JSON-Data
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

def send_Mail(data, PDFfilename):
    #Variablen setzen
    smtp_server="mx2efc.netcup.net"
    mail_sender="anmeldung@zeltlager-braeunlingen.de"
    mail_receiver = data["email"]
    password = os.environ.get('EMAIL_PASSWORD')

    #HTML-Mailbody erstellen und Variable message anhaengen
    htmlbody="""\
    <p>Hallo {} {},<br />
    <br />
    deine Anmeldung hat erfolgreich funktioniert.<br />
    In der angeh&auml;ngten PDF-Datei findest du deine angegebenen Daten.<br />
    Bringe bitte das Formular <u><strong>unterschrieben</strong></u> mit ans Vortreffen.<br />
    <br />
    Viele Gr&uuml;&szlig;e und bis bald!<br />
    Dein Zeltlager</p>
    """.format(data["childFirstName"], data["childLastName"])

    message=MIMEMultipart()
    message["subject"]="Erfolgreiche Anmeldung"
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
            server.sendmail(mail_sender,mail_receiver,message.as_string())
        except:
            return 'mail was not sent, but authentication was successful'
    return 'Mail Sent!'

if __name__ == '__main__':
    app.run(debug=True)