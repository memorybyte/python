"""Sending emails"""

from pathlib import Path
from string import Template # For template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib 

template = Template(Path('template.html').read_text())

message = MIMEMultipart()

message['from'] = 'Memory Byte'
message['to'] = 'pratikpsingh11@gmail.com'
message['subject'] = 'This is a test.'
# message.attach(MIMEText('Body'))
body = template.substitute({'name': 'John'})
message.attach(MIMEText('Body', 'html'))
# message.attach(MIMEImage(Path('path_to_image.png').read_bytes())) # image has to be sent in binary

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(message)
    print('Sent...')