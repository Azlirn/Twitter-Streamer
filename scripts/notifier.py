import gmail_mailer
import datetime


def scriptstart_notify():
    systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
    start_email = """
##### STREAMER RESTARTED #####

System Time: %s

- StreamerBot

***************************************************************************
This is an automated message from the Twitter Streamer.
***************************************************************************
""" % systime
    gmail_mailer.error_message(start_email.encode('utf8'), 'start')
    return

def error_notify(e, all_data):
    systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
    error_email = """
##### ERROR OCCURRED #####

Script error occurred at: %s

Exception occurred: %s

Data: %s

Please report this error to the application admin!

- StreamerBot

***************************************************************************
This is an automated message from the Twitter Streamer.
***************************************************************************
""" % (systime, e, all_data)

    gmail_mailer.error_message(error_email.encode('utf8'), 'system_error')
    return

def notify(data, url, hit):
        systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
        data_text = """
##### NOTIFICATION #####

System Time: %s
Hit Type: %s
Screen Name: %s
Tweeter ID: %s
Tweet Text: %s
Created At: %s
Created Using: %s
Expanded Urls: %s
Tweet Link: https://twitter.com/%s/status/%s\n

- StreamerBot

***************************************************************************
This is an automated message from the Twitter Streamer.

WARNING: THE ABOVE URLS ARE LIVE AND MAY CONTAIN MALICIOUS CODE AND/OR
INAPPROPRIATE CONTENT. USE EXTREME CAUTION!
***************************************************************************

            """ % (systime, hit, data["user"]["screen_name"], data['user']['id'], data["text"], data["created_at"], data["source"], url, str(data['user']['screen_name']), str(data['id']))

        # pass the text to the gmail-mailer script + encode to UTF to deal with none ascii chars
        gmail_mailer.main(data_text.encode('utf8'), hit, data['user']['screen_name'])
        return



def refresh(all_data):
        systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
        refresh_email = """
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
        gmail_mailer.error_message(refresh_email.encode('utf8'), 'backlog_refresh')
        from TwitterStreamer import main
        main()
        return