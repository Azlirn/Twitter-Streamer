import os, time, datetime
import csv
from urlparse import urlparse
import re
import json
import requests
import twitter_setup


# TODO: Change restart countdown to a loop

# Fuction used to at the startup of the program
def print_headers():
    '''
    This function simply asks the OS to clear the existing window
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print "#" * 80
    print "#" + " " * 32 + "Time to Hunt on Twitter!" + " " * 22 + "#"
    print "#" * 80
    time.sleep(1)
    print "Twitter Streamer ver. 2.0"
    print "This version of the Twitter Streamer has been optimized for use by the MS-ISAC"
    print ''
    print "Developed by Philippe Langlois & Christopher Cooley"
    print "#" * 60
    print ''

    time.sleep(5)

def restart_program():
    systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y% %H:%M:%S')

    '''
    This function will restart the application if disconnected after waiting
    a specific amount of time
    '''
    print "*" * 30
    print "[!] Fatal Error - Disconnected at: %s" % systime
    print "*" * 30
    time.sleep(1)

    print "     [!] Attempting to restart script in 60 seconds..."
    time.sleep(10)
    print "     [!] Attempting to restart script in 50 seconds..."
    time.sleep(10)
    print "     [!] Attempting to restart script in 40 seconds..."
    time.sleep(10)
    print "     [!] Attempting to restart script in 30 seconds..."
    time.sleep(10)
    print "     [!] Attempting to restart script in 20 seconds..."
    time.sleep(10)
    print "     [!] Attempting to restart script in 10 seconds..."
    time.sleep(10)
    print "[!] Attempting to restart now..."
    print '\n'
    time.sleep(5)


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
            print " [*] Loading Domains..."
            with open('data/GOV_Domain_list.txt') as f:
                for domain in f.readlines():
                    dom = domain.strip('\n').strip('\r').lower()
                    domains.append(str(dom))
            print " [*] Finished loading %s domains!\n" % len(domains)
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

    print " [*] Loading Twitter Accounts to Monitor..."

    unames = []
    file = open('data/Actor_Profiles.csv', 'rU')
    reader = csv.reader(file)
    # next(reader, None)  # ignore the csv headers
    data = list(reader)

    for row in data:
        parsed = urlparse(row[3])
        unames.append(re.sub('[/]', '', parsed.path))

    print " [**] Finished loading %s accounts!" % len(unames)
    print "\n [*] Converting the account names to their native ID's for persistence..."
    print " [!] NOTE: This will take a while depending on the size of your list..."

    time.sleep(1)
    follower = []

    for u in unames:
        try:
            u_id = str(api.get_user(u, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).id)
            print "     [ + ]", u, "=>", u_id
            follower.append(u_id)
        except Exception, e:
            print "\n"
            print u, "--->", str(e)
            print "\n"
            pass
    return follower


def TwitSLTT_loader():
    """
    Pulls the twitter accounts from the SLTT_TwitterAccounts.csv
    """
    print "\n [*] Loading Twitter accounts for checking against mentions..."
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
            print "     [ + ] Loaded Account:", uname
    print "\n [**] Finished loading %s Twitter accounts!" % len(TwitSLTT)
    return TwitSLTT


def stringify_hashtags_lower(data):
    """
    converts the multiple hashtags referenced into a single string
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
    converts multiple urls in Tweets into a single string
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


def display_tweet(data, hit, trackFound):
    # This presents a view of hits to the analyst
    print '\n'
    print '#' * 40, ' %s' % hit, '#' * 40
    print '\n'
    print "Tweeted By: %s" % str(data['user']['screen_name']), "Tweeter Account ID: %s" % str(data['user']['id'])
    print "Tweet Text: %s" % data['text']
    print "Retweeted? %s" % data['retweeted']
    print "Terms Found: %s" % trackFound
    print "Created At: %s" % data['created_at']
    print "Tweet Link:", "https://twitter.com/%s/status/%s" % (str(data['user']['screen_name']), str(data['id']))
    print "Tweet Mentions: %s" % (stringify_mentions(data))
    print "Tweet Hashtags: %s" % (stringify_hashtags_reg(data))
    print "Expanded Url/s: %s" % (str(stringify_url(data)))
    print "System Time: %s" % (datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S'))
    print '\n'
    print '#' * 40, ' %s' % hit, '#' * 40
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
    print '#' * 20, "Blacklisted Term Found", '#' * 20
    print 'Term Found: ', termfound
    print "Tweet Posted By %s" % str(all_data['user']['screen_name'])
    print "Tweeter Account ID: %s" % str(all_data['user']['id'])
    print "Re-Tweeted? ", all_data['retweeted']
    print "Tweet Text: %s" % all_data['text']
    print "Tweet Link:", "https://twitter.com/%s/status/%s" % (str(all_data['user']['screen_name']), str(all_data['id']))
    print "Tweet Hashtags: ", twitHash
    print "Tweet Mentions: %s" % (stringify_mentions(all_data))
    print "Expanded Url: %s" % (str(stringify_url(all_data)))
    print ''


def disabling_ssl_warning():
    try:
        print "[*] Attempting to disable SSL Warnings..."
        requests.packages.urllib3.disable_warnings()
        print "[**] Complete...\n"
    except:
        print ''
        print '#' * 40
        print "[!] Unable to disable SSL Warnings"
        print '#' * 40
        print ''
        pass
