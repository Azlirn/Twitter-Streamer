Twitter Streamer
================
_Version 2.1_

**We are overhauling this script - please be patient as bugs may be present - open an issue needed**


## Real-Time Twitter Cyber Threat Monitoring Script
The Twitter Streamer is a Python application intended to notify cyber intelligence analysts of cyber threats found on 
Twitter that are targeting specific organizations

---

**How It Works**

The application detects threats through keyword, domain, and Twitter accounts monitoring via the Twitter API. 
After a public threat is posted to Twitter, an automated email notification containing details of the post and the affiliated cyber threat actor is delivered to a specified recipient. 
These details include the platform the Tweet was created with, the unique account ID associated with the actor (which can be used to track down and actor if their screen name changes), geolocation of the tweet (if available), and much more. 
Further analytics may be available depending on the configuration of the application.

### Installation
Currently, the operation of the Twitter Streamer must be done from the command line.
You must have the following to operate this application:

* The applicationw as developed with Debian Linux (other Linux kernels have not been tested - use at your own risk)
* [Internet Connection](http://www.speedtest.net/)
* [Intermediate Python Skills](https://www.codecademy.com/learn/python)
* [Twitter Development Account](https://dev.twitter.com/)
    * You will need to create a Twitter application to obtain API keys to use this program. 
    * https://apps.twitter.com/
* pip is required for the installation of the packages used for this platform. 
    * Install pip: `apt-get install python-pip python-dev build-essential`

### Dependencies

_Keep in mind that basic user accounts will likely need `sudo` access to install dependencies._

* Tweepy
    * To install Tweepy:
    `pip install tweepy`
* oauth2client
    * To install oauth2client:
    `pip install oauth2client`
* httplib2
    * To install httplib2:
    `pip install httplib2`
* smtplib
    * To install smtplib:
    `pip install smtplib`

### How to operate

<PENDING UPDATE>

## Contributors

**Co-Author:** _Philippe Langlois_

* Email: philippe.langlois925@gmail.com
* Github: [planglois925](https://github.com/planglois925)

**Co-Author & Maintainer:** _Chris Cooley_

* Email: chris.cooley@centerforcyberintelligence.org
* Github: [Azlirn](https://github.com/Azlirn)
* Twitter: [@Cyb3rdude](https://twitter.com/cyb3rdude)