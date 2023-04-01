from flask import Flask, request
from flask_cors import CORS, cross_origin
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/registration', methods=['POST'])
@cross_origin()
def submit_data():
    print(request)
    data = request.get_json()
    print(data)
    # do something with the data
    return 'Data received: {}'.format(data)

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