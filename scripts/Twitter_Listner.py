# coding=utf-8

import time
import datetime
import json
import email_mailer
import notifier
import starter
from urlparse import urlparse
from tweepy import API
from tweepy.streaming import StreamListener

reload(email_mailer)
reload(notifier)


class listener(StreamListener):

    def __init__(self, api=None):

        # Variables used throughout the script
        self.api = api or API()
        self.domains = starter.domain_loader()
        self.user_names = starter.username_loader()
        self.accountLoader = starter.account_Loader()
        self.counter_hit_Account = 0
        self.counter_hit_Domain = 0
        self.counter_hit_Keyword = 0
        self.counter_hit = 0
        self.counter_false = 0
        self.counter_all = 0
        self.counter_exception = 0
        self.blacklistcounter = 0
        self.lasttime = datetime.datetime.now()
        self.blacklistLoader = starter.get_blacklist()
        self.trackLoader = starter.get_track()


    def on_data(self, data):
        """
        This part of the script takes in the data sent from Twitter and applies
        different logical functions to it.
        
        Current configuration:
            - Ignores retweets and other terms that have been deemed of no value
            - Checks if URLs mentioned are in the list of domains OR
            - Checks if User mentions are in our list of MentionTwitterAccounts OR
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

                ### DOMAIN TEST ###

                if self.domain_test(all_data):

                    # If a tweet is found, check to see if a blacklisted term is in the tweet. If a blacklisted term
                    # is found, ignore the tweet.
                    if self.blacklist(all_data):
                        pass

                    else:

                        # Hit Type
                        hit = 'DOMAIN MENTION'

                        # Counter increase
                        self.counter_hit_Domain = self.counter_hit_Domain + 1
                        self.counter_hit = self.counter_hit + 1
                        self.counter_all = self.counter_all + 1

                        # Write to JSON
                        starter.write_to_json(all_data, hit)

                        # Notify
                        trackFound = self.termHits(all_data)
                        string_url = starter.stringify_url(all_data)
                        notifier.notify(all_data, string_url, hit, trackFound)

                        # Display
                        starter.display_tweet(all_data, hit, trackFound)

                ###  Account Mention Test  ###

                elif self.accountMention(all_data):

                    # If a tweet is found, check to see if a blacklisted term is in the tweet. If a blacklisted term
                    # is found, ignore the tweet.
                    if self.blacklist(all_data):
                        pass

                    else:
                        # Hit type
                        hit = 'ACCOUNT MENTION'

                        # Counter Increase
                        self.counter_hit_Account = self.counter_hit_Account + 1
                        self.counter_hit = self.counter_hit + 1
                        self.counter_all = self.counter_all + 1

                        # Write to JSON
                        starter.write_to_json(all_data, hit)

                        # Notify
                        trackFound = self.termHits(all_data)
                        string_url = starter.stringify_url(all_data)
                        notifier.notify(all_data, string_url, hit, trackFound)

                        # Display
                        starter.display_tweet(all_data, hit, trackFound)


                ###  CTA Mention Test   ###

                elif str(all_data["user"]["id"]) in self.user_names:

                    # If a tweet is found, check to see if a blacklisted term is in the tweet. If a blacklisted term
                    # is found, ignore the tweet.
                    if self.blacklist(all_data):
                        pass

                    else:
                        # Hit type
                        hit = "KNOWN CTA ACTIVITY"

                        # Counter increase
                        self.counter_hit_Keyword = self.counter_hit_Keyword + 1
                        self.counter_hit = self.counter_hit + 1
                        self.counter_all = self.counter_all + 1

                        # Write to JSON
                        starter.write_to_json(all_data, hit)

                        # Notify
                        trackFound = self.termHits(all_data)
                        string_url = starter.stringify_url(all_data)
                        notifier.notify(all_data, string_url, hit, trackFound)

                        # Display
                        starter.display_tweet(all_data, hit, trackFound)


                # If no logical statement evaluates to True, then count the tweet as a false positive and move on.
                else:
                    self.counter_false = self.counter_false + 1
                    self.counter_all = self.counter_all + 1

            # Every 50,000 Tweets processed, send a health check email to the specified recipients.
            #TODO: Have the emails used for health checks, configured during set up.
            if self.counter_all % 50000 == 0:
                self.health_notify()

        except Exception:
            #TODO: Rework this entire section - this is terrible

            try:
                # Exception to handle messages that indicate Tweets are becoming backlogged.
                if all_data['limit']['track'] >= 10000:
                    print '\n'
                    print "#" * 60
                    print "SYSTEM HAS FALLEN TOO FAR BEHIND AND RISKS CRASHING - AUTO REFRESHING CONNECTION"
                    print "#" * 60
                    print '\n'
                    time.sleep(2)
                    from TwitterStreamer import main
                    print "[!] Restarting Streamer Now..."
                    notifier.refresh(all_data)

                elif all_data['limit']['track'] % 5000 == 0:
                    print '\n'
                    print "#" * 60
                    print "[!] WARNING - SYSTEM IS FALLING BEHIND..."
                    print "#" * 60
                    print '\n'

            except Exception as e:
                self.counter_exception = self.counter_exception + 1
                # Exception to handle 'limit' errors.
                if 'text' or 'limit' in e:
                    print '\nException --> Message: %s\n' % e
                    pass
                else:
                    # Exception to handle any other errors.
                    print "#" * 40
                    print '\nException --> Message: %s\n' % e
                    print ''
                    from notifier import error_notify
                    error_notify('Unknown Listener Error', '--No Data Available--')



    def health_notify(self):
        # TODO: Move this function to notifier.py
        systime = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')
        message = """
                -=This is an automated message from the Twitter Streamer=-

                Server is up...

                System Time: %s
                Total Tweets Processed: %s
                Total Tweets Ignored (Blacklist): %s
                Total Tweets Ignored (False Positive): %s
                Total Hits: %s
                - Breakdown -
                ******************************
                Total Account Mentions: %s
                Total Domain Mentions: %s
                Total Keyword Mentions: %s
                Exceptions raised: %s

    Thanks!
        - StreamerBot""" % (systime, self.counter_all, self.blacklistcounter, self.counter_false, self.counter_hit,
                             self.counter_hit_Account, self.counter_hit_Domain, self.counter_hit_Keyword,
                             self.counter_exception)
        email_mailer.sendEmail(message, 'health_check')
        return


    def blacklist(self, all_data):
        twitText = str(all_data['text'].lower().encode('utf8'))
        twitHash = starter.stringify_hashtags_lower(all_data)
        screenName = str(all_data['user']['screen_name'].lower().encode('utf8'))
        bl = self.blacklistLoader

        # Check to see if the tweet contains a word in our blacklist
        # Checks hashtags, text, and screen names.

        for word in bl:

            if word in twitHash:
                self.blacklistcounter = self.blacklistcounter + 1
                self.counter_all = self.counter_all + 1
                return True

            elif word in twitText:
                self.blacklistcounter = self.blacklistcounter + 1
                self.counter_all = self.counter_all + 1
                return True

            elif word in screenName:
                self.blacklistcounter = self.blacklistcounter + 1
                self.counter_all = self.counter_all + 1
                return True


    def domain_test(self, data):
        '''
        Will test to see if the Urls mentioned are part of the loaded domains.
        '''
        result = []
        try:
            for x in data['entities']['urls']:
                if x['expanded_url'] is not None:
                    result.append(str(urlparse(x["expanded_url"]).netloc).lower() in self.domains)
                else:
                    pass
        except Exception, e:
            print "[!] Domain Test Error: ", str(e)
            return False
        return any(result)


    def accountMention(self, data):
        '''
        Will test to see if the user_mentions screen_name is in MentionTwitterAccounts.csv
        '''

        result = []
        try:
            for x in data['entities']['user_mentions']:
                result.append(x["screen_name"] in self.accountLoader)
        except Exception, e:
            print "[!] Account Mention Error: ", str(e)
            return False
        return any(result)

    def termHits(self, data):
        track = self.trackLoader
        twitData = str(data).lower()

        terms = []

        for term in track:
            if term in twitData:
                terms.append(term)
            else:
                pass
        return terms

    def termInTweetText(self, all_data):
        track = self.trackLoader

        for term in track:
            if term not in all_data['text']:
                return True