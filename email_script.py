import os
import requests
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from bs4 import BeautifulSoup
import template
from dotenv import load_dotenv, dotenv_values 

load_dotenv()

# PART 1: News extraction

# Define the URL for the Google News RSS feed
# url = 'https://news.google.com/rss?hl=en-GB&gl=GB&ceid=GB:en' # UK
url = 'https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it' # Italy

# Fetch the page content using requests
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML content with BeautifulSoup (requires `pip install lxml`)
    soup = BeautifulSoup(response.content, 'lxml-xml')

    news = []

    # Iterate through each item in the XML
    for item in soup.find_all('item'):
        news.append(
            {
                "title": item.title.text,
                "link": item.link.text
            }
            )
else:
    print(f"Failed to fetch the XML data. Status code: {response.status_code}")



email_sender = 'yourmorningfeed@gmail.com'
email_password = os.environ["EMAIL_PASSWORD"]
email_receiver = 'simonepecora@live.it'

subject = 'Your Morning Feed'
body = template.create_html_page(news)

em = EmailMessage()
em = MIMEMultipart("alternative")
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
html_part = MIMEText(body, 'html')
em.attach(html_part)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
