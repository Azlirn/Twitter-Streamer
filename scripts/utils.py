import os
import time
import datetime
import json
import jsonpickle


def stringify_hashtags_lower(data):
    """
    converts the multiple hashtags referenced into a single string
    """
    string_hashtags = []
    hashtag = []
    for item in data.entities['hashtags']:
        hashtag.append(item["text"])
        string_hashtags = ', '.join(hashtag).lower()
    return string_hashtags


def stringify_hashtags_reg(data):
    string_hashtags = []
    hashtag = []
    for item in data.entities['hashtags']:
        hashtag.append(item["text"])
        string_hashtags = ', '.join(hashtag)
    return string_hashtags


def stringify_mentions(data):
    """
    converts multiple user mentions into a single string
    """
    string_user_mentions = []
    user_mention = []

    for x in data.entities['user_mentions']:
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
        for x in data.entities["urls"]:
            if x['expanded_url'] is not None:
                urls.append(x["expanded_url"])
                string_url = ', '.join(urls)
        return string_url
    except Exception as e:
        print("\nERROR - stringify_url Function\n")


def display_tweet(data, hit, trackFound):
    # This presents a view of hits to the analyst
    print('\n')
    print('#' * 40, ' %s' % hit, '#' * 40)
    print('\n')
    print("Tweeted By: %s" % str(data.user.screen_name), "Tweeter Account ID: %s" % str(data.user.id))
    print("Tweet Text: %s" % data.text)
    print("Retweeted? %s" % data.retweeted)
    print("Terms Found: %s" % trackFound)
    print("Created At: %s" % data.created_at)
    print("Tweet Link:", "https://twitter.com/%s/status/%s" % (str(data.user.screen_name), str(data.id)))
    print("Tweet Mentions: %s" % (stringify_mentions(data)))
    print("Tweet Hashtags: %s" % (stringify_hashtags_reg(data)))
    print("Expanded Url/s: %s" % (str(stringify_url(data))))
    print("System Time: %s" % (datetime.datetime.strftime(datetime.datetime.now(), '%m-%d-%Y %H:%M:%S')))
    print('\n')
    print('#' * 40, ' %s' % hit, '#' * 40)
    print('')


def write_to_json(data, hit):
    todayDate = time.strftime("%m-%d-%y")
    directory = os.getcwd() + '/Records/JSON/%s/%s' % (todayDate, hit)

    if not os.path.exists(directory):
        os.makedirs(directory)

    filenmsystime = datetime.datetime.strftime(datetime.datetime.now(), '%H_%M_%S')
    scrnam = str(data.user.screen_name)

    writefile = "%s/%s_%s_%s.json" % (directory, filenmsystime, hit, scrnam)
    jdata = jsonpickle.encode(data)
    with open(writefile, 'w') as outfile:
        json.dump(jdata, outfile)

