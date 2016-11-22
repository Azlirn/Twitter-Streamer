import os, time, subprocess, datetime
import csv
from urlparse import urlparse
import re
import json
import requests
import twitter_setup




#TODO: Change restart countdown to a loop
##### Color Options #####

blk = '\033[0;30m'  # Black - Regular
red = '\033[0;31m'  # Red - Regular
grn = '\033[0;32m'  # Green - Regular
yel = '\033[0;33m'  # Yellow - Regular
blu = '\033[0;34m'  # Blue - Regular
pur = '\033[0;35m'  # Purple - Regular
cyn = '\033[0;36m'  # Cyan - Regular
wht = '\033[0;37m'  # White - Regular
off = '\033[0m'  # Text Reset


#Fuction used to at the startup of the program
def print_headers():
    '''
    This function simply asks the OS to clear the existing window
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print "#" * 80
    print "#" + " " * 32 + "Time to Hunt on Twitter!" + " " * 22 + "#"
    print "#" * 80
    time.sleep(1)
    print blu, "Twitter Streamer ver. 2.1", off
    print red, "This version of the Twitter Streamer is authorized only for use by the MS-ISAC", off
    print ''
    print cyn, "Developed by Philippe Langlois & Chris Cooley", off
    print blu, "#" * 60, off
    print ''

    time.sleep(5)

def restart_program():
    systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y% %H:%M:%S')

    '''
    This function will restart the application if disconnected after waiting
    a specific amount of time
    '''
    print red, "*" * 30, off
    print red, "[!] Fatal Error - Disconnected at: %s" % systime, off
    print red, "*" * 30, off
    time.sleep(1)

    print yel, "     [!] Attempting to restart script in 60 seconds...", off
    time.sleep(10)
    print yel, "     [!] Attempting to restart script in 50 seconds...", off
    time.sleep(10)
    print yel, "     [!] Attempting to restart script in 40 seconds...", off
    time.sleep(10)
    print yel, "     [!] Attempting to restart script in 30 seconds...", off
    time.sleep(10)
    print yel, "     [!] Attempting to restart script in 20 seconds...", off
    time.sleep(10)
    print yel, "     [!] Attempting to restart script in 10 seconds...", off
    time.sleep(10)
    print "[!] Attempting to restart now..."
    print '\n'
    time.sleep(5)

    #PhilEDIT:
    #to fix the problem regarding reloading the the wrong python library
    #uses the python subprocess

    subprocess.call(['bash', '-c', 'source ~/.bashrc'])


def get_track():
    track = [lines.replace('\n','').replace(',','').replace('\r', '').lower() for lines in open('data/track.txt')]
    return track

def get_blacklist():
    blacklist = [lines.replace('\n','').replace(',','').replace('\r', '').lower() for lines in open('data/blacklist.txt')]
    return blacklist

def domain_loader():
        """
        Plus the domains from the file "GOV_Domain_list.csv" from which the
        first row contains the actual domains
        """
        try:
            domains = []
            print blu, "[*] Loading Domains...", off
            with open('data/GOV_Domain_list.txt') as f:
                for domain in f.readlines():
                    dom = domain.strip('\n').strip('\r').lower()
                    domains.append(str(dom))
            print grn, "[*] Finished loading %s domains!\n" % len(domains), off
            return domains
        except:
            print " [!] Error occured while loading domains..."


def username_loader():
    """
        Pulls the malicious actor twitter actors from the actor_profile csv,
        strips the url from the profile name to get access to just the user name
        and tries to search for that screen names User_id
    """
    api = twitter_setup.authenticate_to_twitter()

    print blu, "[*] Loading Twitter Accounts to Monitor...", off

    unames = []
    file = open('data/Actor_Profiles.csv', 'rU')
    reader = csv.reader(file)
    # next(reader, None)  # ignore the csv headers
    data = list(reader)

    for row in data:
        parsed = urlparse(row[3])
        unames.append(re.sub('[/]', '', parsed.path))

    print grn, "[**] Finished loading %s accounts!" % len(unames), off
    print blu, "\n [*] Converting the account names to their native ID's for persistence...", off
    print yel, "[!] NOTE: This will take a while depending on the size of your list...", off

    time.sleep(1)
    follower = []

    for u in unames:
        try:
            u_id = str(api.get_user(u, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).id)
            print grn, "     [ + ]", u, pur, "=>", cyn, u_id, off
            follower.append(u_id)
        except Exception, e:
            print "\n"
            print yel, u, blu, "--->", red, str(e), off
            print "\n"
            pass
    return follower


def TwitSLTT_loader():
    """
    Pulls the twitter accounts from the SLTT_TwitterAccounts.csv
    """
    print blu, "\n [*] Loading Twitter accounts for checking against mentions...", off
    time.sleep(1)
    TwitSLTT = []
    file = open('data/SLTT_TwitterAccounts.csv', 'rU')
    reader = csv.reader(file)
    next(reader, None)  # ignore the csv headers
    data = list(reader)

    for row in data:
        if row[2] == 'Twitter':
            parsed = urlparse(row[3])
            TwitSLTT.append(re.sub('[/]', '', parsed.path))
            uname = re.sub('[/]', '', parsed.path)
            print grn, "     [ + ] Loaded Account:", cyn, uname, off
    print grn, "\n [**] Finished loading %s Twitter accounts!" % len(TwitSLTT), off
    return TwitSLTT


def writeToText(all_data, term):
    todayDate = time.strftime("%d-%m-%y")
    directory = os.getcwd() + '/Records/BlackListTerms/%s' % todayDate

    if not os.path.exists(directory):
        os.makedirs(directory)

    systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y% %H-%M-%S')

    writefile = "%s/BlackListTerms_%s.txt" % (directory, todayDate)
    f = open(writefile, "a")
    text = ("Term Found: %s - Time: %s"
            "\n"
            ) % (term, systime)
    f.write(text.encode('utf8'))
    f.close()

def stringify_hashtags_lower(data):
    """
    converts the multiple url referenced into a single string
    """

    string_hashtags = []
    hashtag = []
    for item in data['entities']['hashtags']:
        hashtag.append(item["text"])
        string_hashtags = ', '.join(hashtag).lower()
    return string_hashtags


def stringify_hashtags_reg(data):

    string_hashtags = []
    hashtag = []
    for item in data['entities']['hashtags']:
        hashtag.append(item["text"])
        string_hashtags = ', '.join(hashtag)
    return string_hashtags


def stringify_mentions(data):
    """
    converts multiple user mentions into a single string
    """

    string_user_mentions = []
    user_mention = []

    for x in data['entities']['user_mentions']:
        user_mention.append(x['name'])
        string_user_mentions = ', '.join(user_mention)
    return string_user_mentions


def stringify_url(data):
    """
    converts the multiple url referenced into a single string
    """

    string_url = []
    urls = []
    try:
        for x in data["entities"]["urls"]:
            if x['expanded_url'] is not None:
                urls.append(x["expanded_url"])
                string_url = ', '.join(urls)
        return string_url
    except Exception as e:
        print "\nERROR - stringify_url Function\n"

# def stringify_media(data):
#     """
#     converts the multiple url referenced into a single string
#     """
#     if 'media' in data:
#         return "FOUND"
#     else:
#         return  "NOT FOUND"
#         # media_url = []
#         # urls = []
#         # for x in data["entities"]["media"]:
#         #     print x
#         #     urls.append(x["media_url_https"])
#         #     media_url = ', '.join(urls)
#         # return media_url


def display_tweet(data, hit, trackFound):
    # This presents a view of hits to the analyst
    print '\n'
    print red, '#' * 40, yel, ' %s' % blu, hit, red, '#' * 40
    print '\n'
    print cyn, "Tweeted By: %s" % pur, str(data['user']['screen_name']), cyn, "Tweeter Account ID: %s" % pur, str(
            data['user']['id']), off
    print grn, "Tweet Text: %s" % wht, data['text'], off
    print grn, "Retweeted? %s" % wht, data['retweeted'], off
    print grn, "Terms Found: %s" % wht, trackFound, off
    print grn, "Created At: %s" % pur, data['created_at'], off
    print grn, "Tweet Link:", blu, "https://twitter.com/%s/status/%s" % (
        str(data['user']['screen_name']), str(data['id'])), off
    # print grn, "Tweet Image Link %s: " % blu, (str(stringify_media(data))), off
    print grn, "Tweet Mentions: %s" % pur, (stringify_mentions(data)), off
    print grn, "Tweet Hashtags: %s" % pur, (stringify_hashtags_reg(data)), off
    print grn, "Expanded Url/s: %s" % blu, (str(stringify_url(data))), off
    print wht, "System Time: %s" % (datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')), off
    print '\n', off
    print red, '#' * 40, yel, ' %s' % blu, hit, red, '#' * 40, off
    print ''


def write_to_json(data, hit):
    todayDate = time.strftime("%m-%d-%y")
    directory = os.getcwd() + '/Records/JSON/%s/%s' % (todayDate, hit)

    if not os.path.exists(directory):
        os.makedirs(directory)

    filenmsystime = datetime.datetime.strftime(datetime.datetime.now(), '%H_%M_%S')
    scrnam = str(data['user']['screen_name'])

    writefile = "%s/%s_%s_%s.json" % (directory, filenmsystime, hit, scrnam)

    with open(writefile, 'w') as outfile:
        json.dump(data, outfile)


def displayBlacklist(all_data, termfound):

    twitHash = stringify_hashtags_lower(all_data)

    print ''
    print yel, '#' * 20, red, "Blacklisted Term Found", yel, '#' * 20, off
    print cyn, 'Term Found: ', grn, termfound, off
    print wht, "Tweet Posted By %s" % red, str(all_data['user']['screen_name']), off
    print cyn, "Tweeter Account ID: %s" % pur, str(all_data['user']['id']), off
    print wht, "Re-Tweeted? ", all_data['retweeted'], off
    print grn, "Tweet Text: %s" % wht, all_data['text'], off
    print grn, "Tweet Link:", blu, "https://twitter.com/%s/status/%s" % (str(all_data['user']['screen_name']), str(all_data['id'])), off
    print blu, "Tweet Hashtags: ", twitHash, off
    print grn, "Tweet Mentions: %s" % pur, (stringify_mentions(all_data)), off
    print grn, "Expanded Url: %s" % blu, (str(stringify_url(all_data))), off
    print ''

def disabling_ssl_warning():
    try:
        print grn, "[*] Attempting to disable SSL Warnings...", off
        time.sleep(2)
        requests.packages.urllib3.disable_warnings()
        print grn, "[**] Complete...\n", off
    except:
        print ''
        print yel, '#' * 40, off
        print red, "[!] Unable to disable SSL Warnings", off
        print yel, '#' * 40, off
        print ''
        pass
