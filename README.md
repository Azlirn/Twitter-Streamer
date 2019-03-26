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

### Installation
Currently, the operation of the Twitter Streamer must be done from the command line.
You must have the following to operate this application:

* The applicationw as developed with Debian Linux (other Linux kernels have not been tested - use at your own risk)
* [Internet Connection](http://www.speedtest.net/)
* [Intermediate Python Skills](https://www.codecademy.com/learn/python)
* [Twitter Development Account](https://dev.twitter.com/)
    * You will need to create a Twitter application to obtain API keys to use this program. 
    * https://apps.twitter.com/

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


## Contributors

**Co-Author:** _Philippe Langlois_

* Email: philippe.langlois925@gmail.com
* Github: [planglois925](https://github.com/planglois925)
* Twitter: [@langlois925](https://twitter.com/langlois925)

**Co-Author & Maintainer:** _Chris Cooley_

* Email: chris.cooley@centerforcyberintelligence.org
* Github: [Azlirn](https://github.com/Azlirn)
* Twitter: [@Cyb3rdude](https://twitter.com/cyb3rdude)