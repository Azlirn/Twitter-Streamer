import tweepy
from .Twitter_Listner import listener



def set_up_listener():
    ckey = "ysXlbDzJePcaTgDUHuTFlQWrS"
    csecret = "3kC7SxMjdDtsoYFB8pwDl6jFbu1tGSGSDqQq6OY3LqqvKe5Fuk"
    atoken = "86768703-0T6rFyAIoKJdLjRD6mTD9V2nvZvah1wPBZ0bru9J8"
    asecret = "B9au0cyO0EM2L01UewFFNyhEdg4S8V2XaNfnEaIxx0r3m"

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    print("[*] Authenticating with Twitter...")
    api = tweepy.API(auth)
    print("[+] Authenticated...\n")

    # set up listener
    print("[*] Setting the tweet \"listener\" up on the stream...")
    listen = listener(api)
    print("[+] Listener is good to go...\n")

    # set up the stream
    print("[*] Turning on the twitter stream...\n")
    return tweepy.Stream(auth, listen)