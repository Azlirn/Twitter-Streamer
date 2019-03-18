#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(text_data, emailType):
    # me == my email address
    # you == recipient's email address
    myEmail = "info@centerforcyberintelligence.org"
    destEmail = "chris.cooley@centerforcyberintelligence.org"

    # Create message container - the correct MIME type is multipart/alternative.
    message = MIMEText(text_data)

    if emailType == 'script_start':
        subject = "[CCI-TS] - Twitter Streamer Started"
        displayType = "Twitter Streamer Started"

    if emailType == 'ALERT':
        subject = "[CCI-TS] - ALERT: Possible Malicious Content Discovered"
        displayType = "ALERT Email"

    message['Subject'] = subject
    message['From'] = myEmail
    message['To'] = destEmail

    # Send the message via local SMTP server.
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    try:
        print " [*] Communicating with mail server..."
        server.login(myEmail, password='S^0VdStM5*ZM60j')
        server.sendmail(myEmail, destEmail, message.as_string())
        print " [*] {%s} email sent successfully...\n" % displayType
    except Exception as e:
        print " [!] Exception Encountered: ", e
        exit()
    server.quit()