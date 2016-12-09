import gmail_mailer
import datetime
import starter


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

def notify(data, url, hit, termFound):
        systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
        data_text = """
##### NOTIFICATION #####

System Time: %s
\rHit Type: %s
\rTerms/s Found: %s
\rScreen Name: %s
\rTweeter ID: %s
\rTweet Text: %s
\rMentions: %s
\rCreated At: %s
\rCreated Using: %s
\rExpanded Urls: %s
\rTweet Link: https://twitter.com/%s/status/%s\n

- StreamerBot

P.S.
"ICA" is a term used to track activity from the Islamic Cyber Army.
Currently, this term, if found, will not appear in the above "Term/s Found" section.
This is a known issue and we are working on a fix.

***************************************************************************
This is an automated message from the Twitter Streamer.

WARNING: THE ABOVE URLS ARE LIVE AND MAY CONTAIN MALICIOUS CODE AND/OR
INAPPROPRIATE CONTENT. USE EXTREME CAUTION!
***************************************************************************

            """ % (systime, hit, termFound, data["user"]["screen_name"], data['user']['id'], data["text"],
                   starter.stringify_mentions(data), data["created_at"], data["source"], url,
                   str(data['user']['screen_name']), str(data['id']))

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