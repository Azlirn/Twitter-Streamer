import tweepy
from .Twitter_Listner import listener



def set_up_listener():

    # Add your Twitter API Keys here

    ckey = ""
    csecret = ""
    atoken = ""
    asecret = ""

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