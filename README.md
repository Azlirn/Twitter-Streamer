Twitter Streamer
================
_Version 2.2_



#### Real-Time OSINT Cyber Threat Monitoring System
The Twitter Streamer is a Python application intended to notify cyber intelligence analysts or a specified audience of cyber threats found on Twitter, that target provided entities.


>In an effort to create a solution that will assist our friends across the cyber landscape, and in support of the open source initiative, we are releasing our Twitter Streamer to whoever feels like filling out an application. However, due to restrictions with Twitters terms of use, the Twitter Streamer is restricted to public and private non-law enforcement use only.
> If you are interested in the Twitter Streamer for your personal or professional use, please fill out our application here: https://goo.gl/forms/zt9dvbOxulB2bvfs2
> We will be in contact with you soon!

---

**History**

My research indicates (and for most cyber intelligence pros out there, it should come as no surprise) cyber threat actors utilize social media platforms as well as personal blogs and websites to issue threats, claims of activity, or to communicate with other threat actors.

In early 2015, we began working on the development of a cyber-focused toolkit that enables cyber intelligence analysts to find, search for, and quickly identify cyber threats to partners sourced from open source information. In mid-2015 it was decided that Twitter would be the first social media platform to tackle.

We began creating a foundation for a tool built with the programming language Python and the integration of the Twitter API. Long story short, and a LOT of Starbucks coffee later, the application is live and is now simply known as the Twitter Streamer. 

---

**How It Works**

The application detects threats through keyword, domain, and Twitter accounts monitoring via the Twitter API. After a public threat is posted to Twitter, an automated email notification containing details of the post and the affiliated cyber threat actor is delivered to a specified recipient. These details include the platform the Tweet was created with, the unique account ID associated with the actor (which can be used to track down and actor if their screen name changes), geolocation of the tweet if available, and much more. Further analytics may be available depending on the configuration of the application.


**Why is this important?**

Before the release of the Twitter Streamer, most cyber intelligence analysts (including myself) needed to monitor individual Twitter accounts manually to find new threats. During development, we acknowledged that applications do exist in the public market that could automate this process however due to tight budgets this is often not a practical solution for many organizations. As an example, throughout 2015, I manually monitored over 120 Twitter accounts daily, searching for cyber threat activity targeting entities related to my day job. The process was incredibly inefficient, taking a considerable amount of time and energy.

The implementation of the Twitter Streamer in any open source cyber threat intelligence program allows analysts to reduce the volume of time focused on conducting manual research on Twitter while the Twitter Streamer simultaneously increases the number of new threats discovered. The Twitter Streamer, based on my current configuration, analyzes 300,000+ tweets, detecting over 200 potential threats, in a 24 hour period. This is a significant achievement that previously would have been unattainable without the use of automation.
 
While the number of potential threats discovered is minuscule compared to the number of tweets analyzed, this figure drives home the point that the amount of manual analysis that would have previously been required to find a potential threat is not an efficient or effective use of resources.
    
---

## Installation
Currently, the operation of the Twitter Streamer must be done from the command line.
You must have the following to operate this application:

* Debian Linux (other Linux kernels have not been tested - use at your own risk)
     * Windows compatibility is not available at this time. 
* [Internet Connection](http://www.speedtest.net/)
* [Intermediate Python Skills](https://www.codecademy.com/learn/python)
* [Twitter Development Account](https://dev.twitter.com/)
    * You will need to create a Twitter application to obtain API keys to use this program. 
    * https://apps.twitter.com/
* pip is required for the installation of the packages used for this platform. 
    * Install pip: `apt-get install python-pip python-dev build-essential`

**Dependencies**

_Keep in mind that basic user accounts will likely need `sudo` access to install dependencies._

* Tweepy
    * To install Tweepy:
    `pip install tweepy`
* [Gmail API](https://developers.google.com/gmail/api/quickstart/python) ( _to be removed in a later version_ )
     * To install the Gmail Python API Library:
     `pip install --upgrade google-api-python-client`
     * Check out other installation options [here](https://developers.google.com/api-client-library/python/start/installation)\
* Mozilla Firefox

* Selenium
    * To install selenium:
    `pip install selenium`


(This section to be updated)

## How to operate

>The streamer is streamlined to run on an Ubuntu AWS instance. We run the streamer via an SSH connection with our AWS instance.  We use `screen` to run our script without an active SSH connection. 

* Screen Basic Tutorial: http://thingsilearned.com/2009/05/26/gnu-screen-super-basic-tutorial/

## Contributors

**Author:** _Philippe Langlois_

* Email: philippe.langlois925@gmail.com
* Github: [planglois925](https://github.com/planglois925)
* Twitter: @

**Co-Author & Maintainer:** _Chris Cooley_

* Email: christopher.a.cooley@gmail.com
* Github: [Azlirn](https://github.com/Azlirn)
* Twitter: [@Cyb3rdude](https://twitter.com/cyb3rdude)

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nd/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Twitter Streamer</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/Azlirn/Twitter-Streamer" property="cc:attributionName" rel="cc:attributionURL">Philippe Langlois and Christopher Cooley</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>.

**Copyright (c) 2016 Philippe Langlois & Christopher Cooley**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software subject to the following conditions:

**You are free to:**

* _Share_ — copy and redistribute the material in any medium or format for any purpose, even commercially.
    * We will not revoke these freedoms as long as everyone plays fair and follows the license terms.

**Under the following terms:**

* _Attribution_ — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* _NoDerivatives_ — If you remix, transform, or build upon the material, you may not distribute the modified material.
    * _However_ we do encourage you to reach out to us to see if your new versions can be added to the existing project.
    
_No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits._

**Notices:**

* You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.
* No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

**The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.**

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**