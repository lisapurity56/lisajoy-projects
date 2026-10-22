import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "youraddress@gmail.com"
recipient = "youraddress@gmail.com"
app_password = "YOUR_16_CHARACTER_APP_PASSWORD"

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
