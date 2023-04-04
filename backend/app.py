from dotenv import load_dotenv
import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import jinja2
import pdfkit

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
    print(data)
    print(send_Mail(data, create_pdf(data)))
    return 'New registration added to database: ' + str(result.inserted_id)

def create_pdf(data):
    template_loader=jinja2.FileSystemLoader('./')
    template_env=jinja2.Environment(loader=template_loader)
    #reads template and replaces the placeholder with the given JSON-Data
    template=template_env.get_template('html-template.html')
    output_text=template.render(data)
    PDFfilename="Anmeldebestaetigung_"+data["childFirstName"]+data["childLastName"]+".pdf"
    #set the location of wkhtmltopdf and it generates the pdf
    config=pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_string(output_text, 'pdf/'+PDFfilename, configuration=config)
    return PDFfilename

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
    """.format(data["childFirstName"],data["childLastName"])

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