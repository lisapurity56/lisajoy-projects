import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "lizajoly78gmail.com"
recipient = "lizajoly78@gmail.com"

app_password = os.getenv("iznnxizigzhstktj")

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = "Test email from Python"

body = "Hello! This is a test message sent in Python."
msg.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, app_password)
    server.send_message(msg)

print("Email sent successfully!")