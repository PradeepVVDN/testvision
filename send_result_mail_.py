import smtplib
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import os
import glob
import imghdr
path="/home/vvdn/Downloads/mtbf_confluence_auto_updated/images"
SENDER_EMAIL = 'pradeepsinh.work@gmail.com'
SENDER_PASSWORD = 'GMAILinside@2'
SERVER = 'smtp.gmail.com:587'
RECEIVER_EMAIL = ['pradeepsinh.dabhi@vvdntech.in','aditya.palwe@vvdntech.in']
SUBJECT = 'Chunichi ________Automation_______'
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
    #ImgFileName = r"/home/vvdn/Downloads/mtbf_confluence_auto_updated/images/dummy1.PNG"
    #ImgFileName = r"/home/vvdn/Downloads/mtbf_confluence_auto_updated/images/report.html"
    #img_data = open(ImgFileName, 'rb').read()
    #img_data2 = open(ImgFileName, 'rb').read()
    #image = MIMEImage(img_data, 'html')
    
    #image.add_header('Content-ID', '<image1>')
    #image.add_header('Content-Disposition', 'inline', filename= ImgFileName)
    #image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    #message.attach(image)

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

    '''
        #message = MIMEMultipart("alternative", None, [MIMEText(HTML, 'html')], [MIMEImage(img)])
        #img.add_header('Content-ID', '<%s>' % img_id)
        #img.add_header('Content-Disposition', 'inline; filename="%s"' % file)
        #
        message.attach(img)
            #message.attach(m)
        fp.close()
  #  message = MIMEMultipart("alternative", None, [MIMEText(HTML, 'html')], [MIMEImage(img,)])
        #message.attach(
         #   MIMEText('<html><body><h1>this is not an image </h1>' + '</body></html>',
          #           'html', 'utf-8'))
        #message.attach(MIMEImage('<p><img src=></p>' + '</body></html>', 'html'))

    #img = cv2.imread(images1)'''
    '''for file in images1:
    #    with open (file, 'rb') as f:
                  image_data = f.read()
                  image_type = imghdr.what(f.name)
                  image_name = f.name
        message.attach(image_data, maintype='image', subtype=image_type, filename=image_name)'''

    


 #   message = MIMEText('<html><body><h1>Hello World</h1>' + '<p>this is hello world from <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 'html', 'utf-8')
 #  with open( "/home/vvdn/Downloads/mtbf_confluence_auto_updated/images/" + "mtbf_report.PNG" , 'rb') as f:
 #      image_data = f.read()
 #    #  image_type = png
 #      image_name = f.name
 #  message.attach(f)

 #  message.attach()


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
