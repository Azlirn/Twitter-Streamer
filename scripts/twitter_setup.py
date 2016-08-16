import tweepy
import Twitter_Listner


def authenticate_to_twitter():
    ckey = "Km42d2CwKsof2SVHybeCQJIl0"
    csecret = "yAVfwoO9cezIDYMw8kvxqKqE4pdb6v5il0nylISKhYsmCiXQ8d"
    atoken = "2871242755-DpeU6UXMMXFDjl27nDmsWbV9XB1IP2TJViKxluH"
    asecret = "qOdzs0V72QkFuhBS1yMFyV3CtKh3nuakSGepOOdxrJbuK"

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    return tweepy.API(auth)

def set_up_listener():
    ckey = "Km42d2CwKsof2SVHybeCQJIl0"
    csecret = "yAVfwoO9cezIDYMw8kvxqKqE4pdb6v5il0nylISKhYsmCiXQ8d"
    atoken = "2871242755-DpeU6UXMMXFDjl27nDmsWbV9XB1IP2TJViKxluH"
    asecret = "qOdzs0V72QkFuhBS1yMFyV3CtKh3nuakSGepOOdxrJbuK"

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    print  " [*]  Authenticating with Twitter"
    api = authenticate_to_twitter()

    # set up listener
    print " [*]  Setting up the API..."
    listen = Twitter_Listner.listener(api)

    # set up the stream
    print "\n[*]  Starting the live stream..."
    return tweepy.Stream(auth, listen)

