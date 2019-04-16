import smtplib
from email.mime.text import MIMEText

def sendEmail(text_data, emailType):
    # me == my email address
    # you == recipient's email address
    myEmail = ""
    destEmail = ""

    # Create message container - the correct MIME type is multipart/alternative.
    message = MIMEText(text_data)

    if emailType == 'script_start':
        subject = "[CCI-TS] - The Twitter Streamer Has Started"
        displayType = "Twitter Streamer Started"

    elif emailType == 'ALERT':
        subject = "[CCI-TS] - ALERT: Possible Malicious Content Discovered"
        displayType = "ALERT Email"

    elif emailType == 'system_error':
        subject = "[CCI-TS] - ERROR: Twitter Streamer Encountered an Error"
        displayType = "Error Email"

    elif emailType == 'health_check':
        subject = "[CCI-TS] - HEALTH CHECK: Twitter Streamer is Running"
        displayType = "Health Check"

    elif emailType == 'backlog_refresh':
        subject = "[CCI-TS] - REFRESH: Twitter Streamer is Restarting"
        displayType = "REFRESH"

    message['Subject'] = subject
    message['From'] = myEmail
    message['To'] = destEmail

    # Send the message via local SMTP server.
    # Example: host='smtp.gmail.com', port=587
    server = smtplib.SMTP(host='', port=)
    server.ehlo()
    server.starttls()
    try:
        print("[*] Communicating with mail server...")
        # Add your password to your email account here
        server.login(myEmail, password='')
        server.sendmail(myEmail, destEmail, message.as_string())
        print("[*] {%s} email sent successfully...\n" % displayType)
    except Exception as e:
        print("[!] Exception Encountered: ", e)
        exit()
    server.quit()