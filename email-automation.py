import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time


# Set your email address
your_email = input('Your email address: ').strip()

# Password
passwd = input('Password: ').strip()

# Set the email recipient
to_email = input("Please enter the recipient email address: ").strip()

# Set the email subject
subject = input('Enter the subject: ').strip()

# Set the file path of the CSV file
csv_file = input('Please enter the file path: ').strip()

# Set the date and time to send the email
send_date = datetime.datetime.now().replace(day=1, hour=8, minute=0, second=0, microsecond=0)

# Calculate the number of seconds between the current time and the send time
time_delta = (send_date - datetime.datetime.now()).total_seconds()

# Wait until the send time
time.sleep(time_delta)

# Create a MIME message object
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = your_email
msg['To'] = to_email

# Attach the CSV file to the email
with open(csv_file, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='csv')
    attachment.add_header('Content-Disposition', 'attachment', filename=csv_file)
    msg.attach(attachment)

# Send the email using SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = your_email
smtp_password = passwd

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, to_email, msg.as_string())
