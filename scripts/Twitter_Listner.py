# coding=utf-8

from tweepy import API
from tweepy.streaming import StreamListener
import gmail_mailer, notifier, starter
import time, datetime, json
from urlparse import urlparse

reload(gmail_mailer)
reload(notifier)

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

###########################


class listener(StreamListener):
    def __init__(self, api=None):

        # Variables used throughout the script
        self.api = api or API()
        self.domains = starter.domain_loader()
        self.user_names = starter.username_loader()
        self.TwitSLTT = starter.TwitSLTT_loader()
        self.counter_hit_SLTT = 0
        self.counter_hit_Domain = 0
        self.counter_hit_Keyword = 0
        self.counter_hit = 0
        self.counter_false = 0
        self.counter_all = 0
        self.counter_exception = 0
        self.blacklistcounter = 0
        self.lasttime = datetime.datetime.now()

    def on_data(self, data):
        """
        This part of the script takes in the data sent from Twitter and applies
        different logical functions to it.
        
        Current configuration:
            - Ignores retweets and other terms that have been deemed of no value
            - Checks if URLs mentioned are in the list of domains OR
            - Checks if User mentions are in our list of SLTT twitter accounts OR
            - Looks to see user id of tweet is from our list of known user names.
        This logical configuration has been optimized to reduce the amount of overall false positives and should not
        be changed.
        """

        all_data = json.loads(data)

        try:
            # Remove re-tweets from the feed.
            if all_data['retweeted']:
                pass

            else:
                if self.domain_test(all_data):
                    if self.blacklist(all_data):
                        pass
                    else:
                        # Hit Type
                        hit = 'SLTT DOMAIN MENTION'

                        # Counter increase
                        self.counter_hit_Domain = self.counter_hit_Domain + 1
                        self.counter_hit = self.counter_hit + 1
                        self.counter_all = self.counter_all + 1

                        # Display
                        starter.display_tweet(all_data, hit)

                        # Notify
                        string_url = starter.stringify_url(all_data)
                        notifier.notify(all_data, string_url, hit)

                        # Write to JSON
                        starter.write_to_json(all_data, hit)

                # Test to see if user_mentions contains partner Twitter Accounts
                elif self.SLTT_mention(all_data):
                    if self.blacklist(all_data):
                        pass
                    else:
                        # Hit type
                        hit = 'SLTT TWITTER MENTION'

                        # Counter Increase
                        self.counter_hit_SLTT = self.counter_hit_SLTT + 1
                        self.counter_hit = self.counter_hit + 1
                        self.counter_all = self.counter_all + 1

                        # Display
                        starter.display_tweet(all_data, hit)

                        # Notify
                        string_url = starter.stringify_url(all_data)
                        notifier.notify(all_data, string_url, hit)

                        # Write to JSON
                        starter.write_to_json(all_data, hit)

                # Test to see if the tweet userid is in your list
                elif str(all_data["user"]["id"]) in self.user_names:
                    if self.blacklist(all_data):
                        pass
                    else:
                        # Hit type
                        hit = "KNOWN THREAT ACTOR ACTIVITY"

                        # Counter increase
                        self.counter_hit_Keyword = self.counter_hit_Keyword + 1
                        self.counter_hit = self.counter_hit + 1
                        self.counter_all = self.counter_all + 1

                        # Display tweet
                        starter.display_tweet(all_data, hit)

                        # Notify
                        string_url = starter.stringify_url(all_data)
                        notifier.notify(all_data, string_url, hit)

                        # Write to JSON
                        starter.write_to_json(all_data, hit)

                # If no logical statement evaluates to True, then count the tweet as a false positive and move on.
                else:
                    self.counter_false = self.counter_false + 1
                    self.counter_all = self.counter_all + 1

            if self.counter_all % 500 == 0:

                print '\n'
                print blu, '#' * 20, grn, "Health Check", blu, '#' * 20, off
                print grn, "Total Tweets Processed:", blu, self.counter_all, off
                print grn, "Total Tweets Ignored (Blacklist):", blu, self.blacklistcounter, off
                print grn, "Total Tweets Ignored (False Positives):", blu, self.counter_false, off
                print wht, "Total Tweets HIT:", cyn, self.counter_hit, off
                print yel, "SLTT Mentions:", pur, self.counter_hit_SLTT, off
                print yel, "Domain Hits:", pur, self.counter_hit_Domain, off
                print yel, "Keyword Mentions:", pur, self.counter_hit_Keyword, off
                print red, "Exceptions Raised:", yel, self.counter_exception, off
                print blu, "System time is:", datetime.datetime.strftime(datetime.datetime.now(),
                                                                         '%m-%d-%Y %H:%M:%S'), off
                print '\n'

            if self.counter_all % 50000 == 0:
                self.health_notify()

        except:

            try:
                if all_data['limit']['track'] >= 10000:
                    print '\n'
                    print yel, "#" * 60, off
                    print red, "SYSTEM HAS FALLEN TOO FAR BEHIND AND RISKS CRASHING - AUTO REFRESHING CONNECTION", off
                    print yel, "#" * 60, off
                    time.sleep(2)
                    from TwitterStreamer import main
                    print yel, "Restarting Streamer Now...", off
                    notifier.refresh(all_data)

                elif all_data['limit']['track'] % 5000 == 0:
                    print '\n'
                    print yel, "#" * 60, off
                    print red, "WARNING - SYSTEM IS FALLING BEHIND", off
                    # print red, "YOU ARE %s TWEETS BEHIND" % all_data['limit']['track'], off
                    print yel, "#" * 60, off

            except Exception as e:
                self.counter_exception = self.counter_exception + 1
                if 'text' or 'limit' in e:
                    pass
                else:
                    print red, "#" * 40, off
                    print yel, 'Exception --> Message: %s' % e
                    print ''
                    from notifier import error_notify
                    error_notify(e, all_data)

    def health_notify(self):
        systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
        health_data = """
                -=This is an automated message from the Twitter Streamer=-

                Server is up...

                System Time: %s
                Total Tweets Processed: %s
                Total Tweets Ignored (Blacklist): %s
                Total Tweets Ignored (False Positive): %s
                Total Hits: %s
                - Breakdown -
                ******************************
                Total SLTT Mentions: %s
                Total Domain Mentions: %s
                Total Keyword Mentions: %s
                Exceptions raised: %s

    Thanks!
        - Cyb3rdude""" % (systime, self.counter_all, self.blacklistcounter, self.counter_false, self.counter_hit,
                             self.counter_hit_SLTT, self.counter_hit_Domain, self.counter_hit_Keyword,
                             self.counter_exception)
        gmail_mailer.health_check(health_data.encode('utf8'))
        return


    def blacklist(self, all_data):
        twitText = str(all_data['text'].lower().encode('utf8'))
        twitHash = starter.stringify_hashtags_lower(all_data)
        # twitMention = self.SLTT_mention(all_data)

        blacklist = ['Trump', 'TRUMP', 'Obama', 'Hillary', 'OpAfrica', 'OpTibet', 'OpJAT', 'Tibet', 'Yemen',
                     'FreeTibet', 'Suspended', 'GhostOfNoNation', 'Germany', 'VTFlintWater', 'Google',
                     'Android', 'Zoophile', 'OpIceISIS', 'DemDebate', 'LibCrib', 'Bernie',
                     'OpIcarus', 'OpIsrael2016', 'OpGuerilla', 'OpWhales', 'OpTrump', 'OpPS', 'OpJAT',
                     'HillaryClinton', 'SeaWorld', 'OpSeaWorld', 'Orcas', 'RT @', 'RT ', 'statistics', 'abortion',
                     'InnovateNAU', '866-561-2500', 'RNA', 'DNA', 'ApplevsFBI', 'WeAreNotThis'
                     'woofwoofwednesday', 'job', 'DBaileyAppeals', 'Administrator', 'Engineer', 'OpOlympicHacking',
                     'OpNimr', 'OpSweden', 'FreeAnons', 'OpWhales', 'OpKillingBay', 'pinterest', 'OpNo2Fur',
                     '0daytoday', 'elpasotimes', 'GresCosette', 'HelenaJobs', 'job', 'jobs', 'Amazon']
        bl = [item.lower() for item in blacklist]
        # Check to see if the tweet contains a word in our blacklist

        for word in bl:
            if word in twitHash:
                termfound = word
                self.blacklistcounter = self.blacklistcounter + 1
                self.counter_all = self.counter_all + 1
                starter.displayBlacklist(all_data, termfound)
                starter.writeToText(all_data, word)
                return True

            elif word in twitText:
                termfound = word
                self.blacklistcounter = self.blacklistcounter + 1
                self.counter_all = self.counter_all + 1
                starter.displayBlacklist(all_data, termfound)
                starter.writeToText(all_data, word)
                return True


    def domain_test(self, data):
        '''
        Will test to see if the Urls mentioned are part of the loaded domains.
        '''

        result = []
        try:
            for x in data['entities']['urls']:
                result.append(str(urlparse(x["expanded_url"]).netloc).lower() in self.domains)
        except Exception, e:
            print str(e)
            return False

        return any(result)



    def SLTT_mention(self, data):
        '''
        Will test to see if the user_mentions screen_name is in the Twitter SLTT
        '''

        result = []
        try:
            for x in data['entities']['user_mentions']:
                result.append(x["screen_name"] in self.TwitSLTT)
        except Exception, e:
            print str(e)
            return False
        return any(result)


##### WISH LIST #####

# Natural Language Processing
# Machine learning