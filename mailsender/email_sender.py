import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "from@gmail.com"
receiver_email = "rcv@mail.ru"
password = "superpass"

message = MIMEMultipart("alternative")
message["Subject"] = "Secret Santa"
message["From"] = sender_email
message["To"] = receiver_email


def read_email_template(file_path):
    with open(file_path, 'r') as f:
        return f.read()


html = read_email_template('mail_tpl.html')

# Turn these into plain/html MIMEText objects
part = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
