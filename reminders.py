import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

import dotenv

dotenv.load_dotenv()
# Email credentials

def send_emails(user_email):

    """
    method to send reminders and reports received from various classes to users
    :param user_email:
    :return:
    """
    sender_email = os.getenv('SENDER_EMAIL')  # Your Gmail address
    app_password = os.getenv('EMAIL_APP_PASSWORD')    # Your Gmail password or app-specific password

    # Recipient email
    receiver_email = user_email  # Recipient's email address example@gmail.com


    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Test Email from Python'

    # Email body
    # body = 'Hello, this is a test email sent from Python with App Password!'

    html_content = """\
    <html>
      <body>
        <h1>Hello!</h1>
        <p>This is an HTML email sent from Python.</p>
        <p><strong>Enjoy coding!</strong></p>
        <a href="https://www.example.com">Click here to visit our website</a>
      </body>
    </html>
    """
    message.attach(MIMEText(html_content, 'html'))

    # Connect to Gmail's SMTP server and send the email
    try:
        # Set up the SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        smtp_server.login(sender_email, app_password)  # Login with App Password

        # Send the email
        smtp_server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email sent successfully!')

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        # Close the server connection
        smtp_server.quit()

send_emails("hamza.helal.d@gmail.com")