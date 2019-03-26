from .email_mailer import sendEmail
import datetime
from .utils import stringify_mentions


def scriptstart_notify():
    systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')

    message = """
##### STREAMER STARTED #####

System Time: %s

- StreamerBot

***************************************************************************
This is an automated message from the Twitter Streamer.
***************************************************************************
""" % systime

    sendEmail(message, "script_start")
    return

def error_notify(e, all_data):
    systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
    message = """
##### ERROR OCCURRED #####

Script error occurred at: %s

Exception occurred: %s

Data: %s

Please report this error to the application admin!

- StreamerBot

***************************************************************************
This is an automated message from the Twitter Streamer.
***************************************************************************
""" % (systime, e, all_data.text)

    sendEmail(message, 'system_error')
    return

def notify(data, url, hit, termFound):
        systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
        message = """
##### NOTIFICATION #####

System Time: %s
Hit Type: %s
Terms/s Found: %s
Screen Name: %s
Tweeter ID: %s
Tweet Text: %s
Mentions: %s
Created At: %s
Created Using: %s
Expanded Urls: %s
Tweet Link: https://twitter.com/%s/status/%s

- StreamerBot

***************************************************************************
This is an automated message from the Twitter Streamer.

WARNING: THE ABOVE URLS ARE LIVE AND MAY CONTAIN MALICIOUS CODE AND/OR INAPPROPRIATE CONTENT. USE EXTREME CAUTION!
***************************************************************************

            """ % (systime, hit, termFound, data.user.screen_name, data.user.id, data.text,
                   stringify_mentions(data), data.created_at, data.source, url,
                   str(data.user.screen_name), str(data.id))

        # pass the text to the gmail-mailer script + encode to UTF to deal with none ascii chars
        sendEmail(message, "ALERT")
        return



def refresh(all_data):
        systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
        message = """
##### SYSTEM REFRESH #####

System Time is:  %s
The streamer is having a hard time keeping up.

You are currently %s tweets behind.

I am refreshing your connection to purge the cache with the Twitter API.

The tweets in the stream that are backlogged will be lost in this process.

- StreamerBot

***************************************************************************
This is an automated message from the Twitter Streamer.
***************************************************************************
""" % (systime, all_data['limit']['track'])
        sendEmail(message, 'backlog_refresh')
        from TwitterStreamer import main
        main()
        return