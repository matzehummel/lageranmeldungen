from dotenv import load_dotenv
import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import smtplib, ssl
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
    #pdf = create_pdf
    #send_Mail(pdf)
    return 'New registration added to database: ' + str(result.inserted_id)

def send_Mail():
    smtp_server="mx2efc.netcup.net"
    mail_sender="anmeldung@zeltlager-braeunlingen.de"
    mail_receiver="johannesdold2002@gmail.com"
    password=input("type mail-password:")

    body="<p>Hallo</p>"

    message=MIMEMultipart("alternative")
    message["subject"]="Erfolgreiche Anmeldung"
    message["From"]=mail_sender
    message["To"]=mail_receiver
    messagebody=MIMEText(body, "html")
    message.attach(messagebody)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server,port=465,context=context) as server:
        server.login(mail_sender,password)
        server.sendmail(mail_sender,mail_receiver,message.as_string())
    


if __name__ == '__main__':
    app.run(debug=True)
    #send_Mail()
    #submit_data()