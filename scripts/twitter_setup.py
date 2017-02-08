import tweepy
import Twitter_Listner


def authenticate_to_twitter():
    ckey = "ysXlbDzJePcaTgDUHuTFlQWrS"
    csecret = "3kC7SxMjdDtsoYFB8pwDl6jFbu1tGSGSDqQq6OY3LqqvKe5Fuk"
    atoken = "86768703-0T6rFyAIoKJdLjRD6mTD9V2nvZvah1wPBZ0bru9J8"
    asecret = "B9au0cyO0EM2L01UewFFNyhEdg4S8V2XaNfnEaIxx0r3m"

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    return tweepy.API(auth)

def set_up_listener():
    ckey = "ysXlbDzJePcaTgDUHuTFlQWrS"
    csecret = "3kC7SxMjdDtsoYFB8pwDl6jFbu1tGSGSDqQq6OY3LqqvKe5Fuk"
    atoken = "86768703-0T6rFyAIoKJdLjRD6mTD9V2nvZvah1wPBZ0bru9J8"
    asecret = "B9au0cyO0EM2L01UewFFNyhEdg4S8V2XaNfnEaIxx0r3m"

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    print " [*]  Authenticating with Twitter"
    api = authenticate_to_twitter()

    # set up listener
    print " [*]  Setting up the API..."
    listen = Twitter_Listner.listener(api)

    # set up the stream
    print "\n [*]  Starting the live stream..."
    return tweepy.Stream(auth, listen)

