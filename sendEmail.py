# import packages
# below packages are built-in - no need to install anything new!
#https://mljar.com/blog/python-send-email/
import smtplib
from email.message import EmailMessage

import os
from dotenv import load_dotenv
_ = load_dotenv()

# set your email and password
# please use App Password
email_address = os.environ.get("EMAIL_ADDRESS")
email_password = os.environ.get("EMAIL_PASSWORD")

# create email
msg = EmailMessage()
msg['Subject'] = "Email subject"
msg['From'] = email_address
msg['To'] = "to-address@gmail.com"
msg.set_content("This is eamil message")

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)