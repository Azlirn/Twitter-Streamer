Twitter Streamer
================
_Version 3.0_

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Twitter Streamer</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://centerforcyberintelligence.org/" property="cc:attributionName" rel="cc:attributionURL">Center for Cyber Intelligence</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Real-Time Twitter Cyber Threat Monitoring Script
The Twitter Streamer is a Python application intended to notify cyber intelligence analysts of cyber threats found on 
Twitter that are targeting specific organizations

---

**How It Works**

The application detects threats through keyword, domain, and Twitter accounts monitoring via the Twitter API. 
After a public threat is posted to Twitter, an automated email notification containing details of the post and the affiliated cyber threat actor is delivered to a specified recipient. 
These details include the platform the Tweet was created with, the unique account ID associated with the actor (which can be used to track down and actor if their screen name changes), geolocation of the tweet (if available), and much more. 
Further analytics may be available depending on the configuration of the application.

---


### Dependencies

* **Python 3.7.x**

* `pip`
   * To install `pip` with Python 3.7.x: `apt-get install python3-pip`
   
* **certifi** | Version 2019.3.9
    * _This package is included by default in the Python 3.7 distro._
    * `python 3.7 -m pip install certifi`
* **chardet** | Version 3.0.4
    * _This package is included by default in the Python 3.7 distro._
    * `python3.7 -m pip install chardet`
* **idna** | Version 2.8
    * _This package is included by default in the Python 3.7 distro._
    * `python3.7 -m pip install idna`
* **jsonpickle** | Version 1.1
    * `python3.7 -m pip install jsonpickle`
* **Markdown** | Version 3.1
    * `python3.7 -m pip install Markdown`
* **oauthlib** | Version 3.0.1
    * _This package is included by default in the Python 3.7 distro._
    * `python3.7 -m pip install oauthlib`
* **PySocks** | Version 1.6.8
    * _This package is included by default in the Python 3.7 distro._
    * `python3.7 -m pip install PySocks`
* **pytz** | Version 2018.9
    * `python3.7 -m pip install pytz`
* **requests** | Version 2.21.0
    * `python3.7 -m pip install requests`
* **requests-oauthlib** | Version 1.2.0
    * `python3.7 -m pip install requests-oauthlib`
* **six** | Version 1.12.0
    * _This package is included by default in the Python 3.7 distro._
    * `python3.7 -m pip install six`
* **tweepy** | Version 3.7.0
    * `python3.7 -m pip install tweepy`
* **urllib3** | Version 1.24.1
    * _This package is included by default in the Python 3.7 distro._
    * `python3.7 -m pip install urllib3`

### Installation
Currently, the operation of the Twitter Streamer must be done from the command line.
You must have the following to operate this application:

* The applicationw as developed with Debian Linux (other Linux kernels have not been tested - use at your own risk)
* [Internet Connection](http://www.speedtest.net/)
* [Intermediate Python Skills](https://www.codecademy.com/learn/python)
* [Twitter Development Account](https://dev.twitter.com/)
    * You will need to create a Twitter application to obtain API keys to use this program. 
    * https://apps.twitter.com/
---
### Set-up

#### Twitter API Keys
Without Twitter API keys you will be unable to use this script. You will need your "Client Key," "Client Secret," "Authentication Token," and your "Authentication Key."

When you have obtained these keys, head over to the `\Twitter Streamer\scripts\starter.py` file and enter your keys into the quotes in the following variables:

* **Client Key** | Line 11: `ckey = ""`
* **Client Secret** | Line 12: `csecret = ""`
* **Authentication Token** | Line 13: `atoken = ""`
* **Authentication Secret** | Line 14: `asecret = ""`

You will also need to add the same information to the `twitter_setup.py` file. 

* **Client Key** | Line 10: `ckey = ""`
* **Client Secret** | Line 11: `csecret = ""`
* **Authentication Token** | Line 12: `atoken = ""`
* **Authentication Secret** | Line 13: `asecret = ""`

This information _does_ remain hard coded into the script. With this being said, remain mindful of the security measures you have in place on the system you will be running this script from.

#### Receiving Email Alerts
Currently, the script is configured to send a few different types of emails while running. You will receive a "health check" email each 50,000 tweets processed. The frequency in which you will receive this email largely depends on the keywords used when setting up your streamer. If you find you are receivign too many "health check" emails, you can change the number of tweets that must be processed before triggering the email:

##### Health Check Email Configuration
1. Open `\Twitter Streamer\scripts\Twitter_Listener.py` and go to line 101
2. Adjust the number "50000" to a number that suits you in the following code: `if self.counter_all % 50000 == 0:`

##### Altering Email Formats
Currently the Twitter Streamer supports only simple text based emails. You can change subject lines and email body content in the following files:
* **Email Subject Lines** | `\Twitter Streamer\scripts\email_mailer.py` | Line 14: Twitter Streamer Starts; Line 18: Alerting that some "bad" stuff may have been found; Line 22: Some error was encountered; Line 26: Health Check email; Line 30: If the twitter streamer crashes and restarts, this email will be sent to let you know it is restarting
* **Email Body** | `\Twitter Streamer\scripts\notifier.py` _(keep in mind that altering any variables within the body of the email may break the script)_ | Email types should be fairly self explanatory when reviewing the code

##### Setting Up "From" and "To" Addresses
Email alerts are sent using SMTP - The following instructions assume that you have already configured an email client to send and receive emails using SMTP.

1. Head over to the `\Twitter Streamer\scripts\email_mailer.py` file
2. In the variable name `myEmail` on line 7, enter the email address you would like Twitter Streamer alerts to come from.
3. In the variable name `destEmail` on line 8, enter the email address of the recipient for your Twitter Streamer alerts. 
4. On line 39, configure your SMTP server - For example, if you are using Gmail to send your emails, your code should look something like `server = smtplib.SMTP(host='smtp.gmail.com', port=587)`
5. On line 45, you will need to add the password to the email address contained within line 7. For example your code should look something like `server.login(myEmail, password='ThisIs@T3rribl3P@ssw0rd')`

#### Data Configuration
In order for the Twitter Streamer to work, you need to give it some data to dig through. First, you need to have some keywords for it to use to grab a pool of tweets to logically parse through. 

**Any time you update any of these files, you will need to restart your streamer in order for changes to take effect**

##### Keywords
1. Open `\Twitter Streamer\data\KeyWords.txt`
2. Enter your keywords, comma separated, each word on a new line. _Example:_
    
    ```
    DDoS,
    TangoDown,
    Targeted,
    Anonymous
    ```
3. Save

##### Adding Blacklist Entries
At times you may notice that you are receiving multiple alerts that meet your logical criteria (domain, keyword, twitter account, etc.) however the information may be of no value. In version 2.0 we introduced a blacklist function that should assist in reducing these kinds of alerts. Similarly to the keywords list, you can add terms to the blacklist. 
1. Open `\Twitter Streamer\data\Blacklist.txt`
2. Enter your blacklist terms, comma separated, each word on a new line. _Example:_
    
    ```
    OpTrump,
    Logitec,
    Anonymous,
    Microsoft
    ```
3. Save

##### Adding Cyber Threat Actors
The Twitter Streamer extracts needed data from Twitter Profile links each time it starts, in order to track cyber threat actor activity. Currently, while the Streamer does track cyber threat actor activity by the associated account ID (rather than the screen name) this function is not persistent. Meaning, should the screen name of your target threat actor change during a period in which the streamer is not running, when the streamer restarts, you will no longer "see" activity from the given threat actor. If any errors are encountered while loading a cyber threat actor account, you can check the file `\Twitter Streamer\data\CyberActorLoadingErrors.csv` for more information.
Further, you are only able to see publicly available data. The Twitter Streamer does not have the capability to see activity contained in private accounts. 

1. Open `\Twitter Streamer\data\CyberActorAccounts.csv`
2. Enter links to Twitter accounts, comma separated, each account on a new line. _Example:_
    
    ```
    https://twitter.com/centerforintel,
    https://twitter.com/cyb3rdude,
    https://twitter.com/langlois925
    ```
3. Save

##### Adding Domains
In order to hunt for domains on Twitter, you will need to add them to the file `\Twitter Streamer\data\DomainList.txt`

1. Open `\Twitter Streamer\data\DomainList.txt`
2. Enter domains, comma separated, each domain on a new line. _Example:_
    
    ```
    centerforcyberintelligence.org,
    google.com,
    haveibeenpwned.com
    ```
3. Save

##### Adding Accounts to Monitor for Mentions
The twitter streamer can check tweets for mentions of specific twitter accounts. This functionality is useful if you want to check for possible threat actors "mentioning an organizations Twitter account in a tweet.

1. Open `\Twitter Streamer\data\MentionTwitterAccounts.csv`
2. Enter links to Twitter accounts, comma separated, each account on a new line. _Example:_
    
    ```
    https://twitter.com/centerforintel,
    https://twitter.com/cyb3rdude,
    https://twitter.com/langlois925
    ```
3. Save


**You should be good to go at this point!**

---

### Starting The Twitter Streamer
1. Navigate to the directory you have the Twitter Streamer saved
2. Run the command `python3.7 TwitterStreamer.py`
3. Wait for your alerts to come in!

---

## Contributors

**Co-Author:** _Philippe Langlois_

* Email: philippe.langlois925@gmail.com
* Github: [planglois925](https://github.com/planglois925)
* Twitter: [@langlois925](https://twitter.com/langlois925)

**Co-Author:** _Chris Cooley_

* Email: chris.cooley@centerforcyberintelligence.org
* Github: [Azlirn](https://github.com/Azlirn)
* Twitter: [@Cyb3rdude](https://twitter.com/cyb3rdude)