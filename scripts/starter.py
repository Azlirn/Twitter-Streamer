import os
import time
import datetime
import csv
import re
import requests
from urllib import parse
import tweepy

def authenticate_to_twitter():
    ckey = ""
    csecret = ""
    atoken = ""
    asecret = ""

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    return tweepy.API(auth)


def print_headers():
    #TODO: Add a reference for the source code in the title
    """
    This function simply asks the OS to clear the existing window and presents a "title"
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 80)
    print("#" + " " * 18 + "Time to Hunt for Cyber Threats on Twitter!" + " " * 18 + "#")
    print("#" * 80)
    print("Twitter Streamer ver. 2.1")
    print("This version of the Twitter Streamer has been optimized for public use.\n")
    print("Developed by @langlois925 & @cyb3rdude")
    print("#" * 80, '\n')
    time.sleep(5)


def restart_program():
    # TODO: Change restart countdown to a loop
    """
    This function will restart the script after 60 seconds if an Exception is triggered in the main() function in
    TwitterStreamer.py
    """
    systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y% %H:%M:%S')
    print("*" * 30)
    print("[!] Fatal Error - Disconnected at: %s" % systime)
    print("*" * 30)
    time.sleep(1)

    print("     [!] Attempting to restart script in 60 seconds...")
    time.sleep(10)
    print("     [!] Attempting to restart script in 50 seconds...")
    time.sleep(10)
    print("     [!] Attempting to restart script in 40 seconds...")
    time.sleep(10)
    print("     [!] Attempting to restart script in 30 seconds...")
    time.sleep(10)
    print("     [!] Attempting to restart script in 20 seconds...")
    time.sleep(10)
    print("     [!] Attempting to restart script in 10 seconds...")
    time.sleep(10)
    print("[!] Attempting to restart script now...")
    print('\n')
    time.sleep(5)


def get_track():
    """
    This function pulls keywords from KeyWords.txt and preps them to be sent to the Twitter API
    """
    track = [lines.replace('\n','').replace(',','').replace('\r', '').lower() for lines in open('data/KeyWords.txt')]
    return track


def get_blacklist():
    """
    This function pulls terms from Blacklist.txt to be used in Twitter_Listener.py allowing users to ignore keywords
    from Twitter Streamer Alerts
    """
    blacklist = [lines.replace('\n','').replace(',','').replace('\r', '').lower() for lines in open('data/Blacklist.txt')]
    return blacklist


def domain_loader():
    """
    This function loads domains saved in DomainList.txt to be checked against tweets in the stream.
    The output of this function is used in Twitter_Listener.py
    """

    try:
        domains = []
        print("[*] Loading Domains...")
        with open('data/DomainList.txt') as f:
            for domain in f.readlines():
                dom = domain.strip('\n').strip('\r').lower()
                domains.append(str(dom))
        print("[+] Finished loading %s domains...\n" % len(domains))
        return domains
    except Exception as e:
        print("[!] Error occurred while loading domains - %s" % e)


def save_usernameErrors(username, exception):
    """
    This function will save any errors encountered while attempting to convert cyber threat actor twitter accounts to
    twitter IDs into a .csv file for reference at a later date.
    """
    with open("data/CyberThreatActorLoadingErrors.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([username, exception, datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')])
    f.close()


def username_loader():

    #TODO: Add a capability to update values in the .csv if a screen name changes; requires to capture and store
    # Twitter ID

    #TODO: Add a capability to remove a Twitter Account and all related data if it is detected that the account has
    # been deleted.

    """
    Pulls cyber threat actor twitter accounts from the CyberActorAccounts.csv, strips the profile name from the url and
    converts the screen name to a Twitter ID. This ensures that, should the screen name change, you do not lose
    visibility of the actor.
    """
    api = authenticate_to_twitter()

    print("[*] Loading Cyber Threat Actor Twitter Accounts...")

    unames = []
    file = open('data/CyberActorAccounts.csv', 'rU')
    reader = csv.reader(file)
    # next(reader, None)  # ignore the csv headers
    data = list(reader)

    for row in data:
        # Ensure your CyberActorAccounts.csv file has the link to the Twitter account in the first "column" of the .csv
        parsed = parse.urlparse(row[0])
        unames.append(re.sub('[/]', '', parsed.path))

    print("[*] Finished loading %s accounts...\n" % len(unames))
    print("[*] Converting Cyber Threat Actor Twitter Account names to Twitter ID's for persistence...")
    print("[!] NOTE: This will take a while depending on the size of your Cyber Threat Actor list...\n")

    follower = []

    for u in unames:
        try:
            u_id = str(api.get_user(u, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).id)
            print("[+]", u, "=>", u_id)
            follower.append(u_id)
        except Exception as e:
            # TODO: Break apart the exception "dictionary" to display exceptions in a more human readable format
            # Exception Example: [{u'message': u'User not found.', u'code': 50}]

            # Save any exceptions encountered to CyberThreatActorLoadingErrors.csv
            save_usernameErrors(u, e)
            print("\n[!]", u, "=>", str(e), '\n')
            pass
    return follower

def account_Loader():
    """
    Pulls the twitter accounts from the MentionTwitterAccounts.csv
    """
    print("\n[*] Loading \"GOOD\" Twitter accounts so we can check for mentions in \"BAD\" tweets...\n")
    time.sleep(1)
    twitterAccounts = []
    file = open('data/MentionTwitterAccounts.csv', 'rU')
    reader = csv.reader(file)
    data = list(reader)

    for row in data:
        parsed = parse.urlparse(row[0])
        twitterAccounts.append(re.sub('[/]', '', parsed.path))
        uname = re.sub('[/]', '', parsed.path)
        print("[+] Loaded Account:", uname)
    print("\n[*] Finished loading %s \"GOOD\" Twitter accounts..." % len(twitterAccounts))
    return twitterAccounts

def disabling_ssl_warning():
    try:
        print("[*] Attempting to disable SSL Warnings...")
        requests.packages.urllib3.disable_warnings()
        print("[*] SSL Warnings disabled...\n")
    except Exception as e:
        print("[!] Failed to disable SSL Warnings - %s" % e)
        pass