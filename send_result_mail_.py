import smtplib
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import os
import glob
import imghdr
path="PATHOFTHEIMAGE/images"
SENDER_EMAIL = 'XXXXXXXXXXXXX@gmail.com'
SENDER_PASSWORD = 'XXXXXXXXXXXXXX'
SERVER = 'smtp.gmail.com:587'
RECEIVER_EMAIL = ['XXXXXXXXXXXXX@gmail.com','XXXXXXXXXXXXX@gmail.com']
SUBJECT = 'Test_Vision_Framework'
HTML = """
<html>
  <body>
    <p><b>Python Mail Test</b><br>
       This is HTML email with attachment.<br>
       Click on <a href="report.html">REsult_report</a> 
       for more python articles.
    </p>
  </body>
</html>
"""


def _generate_message() -> MIMEMultipart():
    message = MIMEMultipart("alternative", None, [MIMEText(HTML, 'html')])
    message['Subject'] = SUBJECT
    message['From'] = SENDER_EMAIL
    message['To'] = ','.join(RECEIVER_EMAIL)


    with open("report.html", "rb") as attachment:
       part1 = MIMEBase("application", "octet-stream")
       part1.set_payload(attachment.read())
       encoders.encode_base64(part1)
       part1.add_header("Content-Disposition", "attachment", filename= "report.html" )
    message.attach(part1)
    with open("log.html", "rb") as attachment:
       part2 = MIMEBase("application", "octet-stream")
       part2.set_payload(attachment.read())
       encoders.encode_base64(part2)
       part2.add_header("Content-Disposition", "attachment", filename= "log.html" )
    message.attach(part2)
    return message


def send_message():
    message = _generate_message()
    server = smtplib.SMTP(SERVER)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
    server.quit()


if __name__ == '__main__':
    send_message()
