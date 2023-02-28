import smtplib
import ssl
from email.message import EmailMessage
import os


# Set your email address
your_email = input('Your email address: ').strip()

password = 'ovxfgenlpaddttzp'
# Set the email recipient
to_email = input("Please enter the recipient email address: ").strip()

# Set the email subject
subject = input('Enter the subject: ').strip()

# Set the file path of the CSV file
csv_file = input('Please enter the file path: ').strip()

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = your_email
msg['To'] = to_email
msg.set_content('Your email message')

# Add the attachment to the email
attachment_path = '/Users/samarman/Desktop/Python/Ooredoo/Ticketdata.csv'
with open(attachment_path, 'rb') as f:
    file_data = f.read()
    file_name = os.path.basename(attachment_path)
msg.add_attachment(file_data, maintype='application', subtype='csv', filename=file_name)

# Send the email
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = your_email
smtp_password = 'qvcbzavuiicqxqff'

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.send_message(msg)
