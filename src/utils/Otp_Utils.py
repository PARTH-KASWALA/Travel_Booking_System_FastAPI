import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Email configuration
sender_email = "parthkaswala2000@gmail.com"
receiver_email = "parthkaswala95@gmail.com"
password = "mydeoqcuaujnqpbz"
subject = "Your OTP Code"
otp = generate_otp()  # Generate OTP
message_text = f"Your OTP is {otp} which is valid for 1 minute" 

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the message text
message.attach(MIMEText(message_text, "plain"))

# Send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Mail sent successfully")
    server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")








