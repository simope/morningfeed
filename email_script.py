import os
from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'yourmorningfeed@gmail.com'
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = 'simonepecora@live.it'

subject = 'Email subject'
body = """
<h2> Body of the email. </h2>
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
