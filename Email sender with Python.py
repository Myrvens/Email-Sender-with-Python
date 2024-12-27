import os
import ssl
import smtplib
from email.message import EmailMessage

# Load sensitive information from environment variables
email_sender = os.getenv("EMAIL_SENDER")  # Set this as an environment variable for my Gmail address
email_password = os.getenv("EMAIL_PASSWORD")  # Use App Password for my Gmail
email_receiver = "receiver@example.com"  # Replace with the receiver's email address

# Names for sender and receiver
sender_name = "Myrvens Sylvestre"
receiver_name = "Jonathan"

# Email content
subject = "How you can easily send email to another user using Python"
body = f"""
Hi {receiver_name},

Please follow my code to be able to do it.

Best regards,
{sender_name}
"""

# Create the email message
em = EmailMessage()
# Set 'From' with my name and email
em["From"] = f"{sender_name} <{email_sender}>"
# Set 'To' with receiver's name and email
em["To"] = f"{receiver_name} <{email_receiver}>"
em["Subject"] = subject
em.set_content(body)

# Establish a secure SSL context
context = ssl.create_default_context()

try:
    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)  # Log in to my Gmail account
        smtp.sendmail(email_sender, email_receiver, em.as_string())  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
