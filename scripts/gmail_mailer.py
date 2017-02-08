import httplib2
import base64
from time import strftime
from email.mime.text import MIMEText
from apiclient.discovery import build
import oauth2client
from oauth2client import client
from oauth2client import tools

###TODO: Remove duplicate code such as the TO:,From: Fields

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Twit Notifier'
to_address = 'christopher.cooley@cisecurity.org', 'matthew.grieco@cisecurity.org'
from_address = 'spider.sec070@gmail.com'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    # home_dir = os.path.expanduser('~')
    # credential_dir = os.path.join(home_dir, '.credentials')
    # if not os.path.exists(credential_dir):
    #   os.makedirs(credential_dir)
    # credential_path = os.path.join(credential_dir,
    #                              'gmail-quickstart.json')

    store = oauth2client.file.Storage('credential/gmail-quickstart.json')
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to '
    return credentials


def main(text_data, hittype, username):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())

    # Build the Gmail service from discovery
    gmail_service = build('gmail', 'v1', http=http)

    # Create a message to send
    message = MIMEText(text_data)
    message['to'] = to_address
    message['from'] = from_address
    message['subject'] = '%s Notification for CTA %s' % (hittype, username)
    body = {'raw': base64.urlsafe_b64encode(message.as_string())}

    # send it
    try:
        message = (gmail_service.users().messages().send(userId="me", body=body).execute())
        print " [*] Notification Email Sent - Message ID: %s" % message['id']
    except Exception as error:
        print ' [!] An error occurred while attempting to send a notification email: %s' % error


def error_message(email, types):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())

    # Build the Gmail service from discovery
    gmail_service = build('gmail', 'v1', http=http)

    message = MIMEText(email)
    message['to'] = to_address
    message['from'] = from_address

    if types == 'start':
        subject = 'STREAMER RESTARTED at %s' % strftime("%Y-%m-%d %H:%M:%S")
        print_message = '[*] System start email sent - Message ID: %s'

    elif types == 'system_error':
        subject = '[!] Twitter Streamer Error - %s' % strftime("%Y-%m-%d %H:%M:%S")
        print_message = ' [*] Streamer Error email sent - Message ID: %s'

    elif types == 'health_check':
        subject = 'Twitter Health Check: %s' % (strftime("%Y-%m-%d %H:%M:%S"))
        print_message = ' [*] Health Check Email Sent - Message ID: %s'

    elif types == 'backlog_refresh':
        subject = '[!] Twitter Streamer is overloaded - RESTARTING'
        print_message = ' [*] Refresh Email Sent - Message ID: %s'



    message['subject'] = subject
    body = {'raw': base64.urlsafe_b64encode(message.as_string())}
    try:
        message = (gmail_service.users().messages().send(userId="me", body=body).execute())
        print print_message % message['id']
        print '\n'
    except Exception as error:
        print '[!] An error occurred (Error: %s) at %s while sending a %s' % (error, strftime("%Y-%m-%d %H:%M:%S"), types)

if __name__ == '__main__':
    main()