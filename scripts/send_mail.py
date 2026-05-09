import smtplib
from email.mime.text import MIMEText
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Expected format: python send_mail.py "to@email.com" "Subject" "Message body"

if len(sys.argv) < 4:
    print("Usage: python send_mail.py <to_email> <subject> <body>")
    sys.exit(1)

to_email = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3]

GMAIL_USER = "your_email@gmail.com"
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = GMAIL_USER
msg['To'] = to_email

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.send_message(msg)
    print(f"Email sent successfully to {to_email}")
except Exception as e:
    print(f"Failed to send email: {e}")
