import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os



def send_notification_via_email(receiver_email: str, message: str):
    sender_email = os.getenv("sender_email")
    password = os.getenv("password")
    subject = "Notification"
    message_text = message

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message_text, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Notification sent to {receiver_email}: {message}")
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False