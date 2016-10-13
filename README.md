Twitter Streamer
================
_Version 2.2_

### Version 2.2 Released!

Screenshots are now taken of all hits and saved in the Records folder under Screenshots. 
This functionality is only available on Linux platforms at this time and has not been tested on other platforms. 
This new feature may break functionality with OSX platforms. 



#### Real-Time OSINT Cyber Threat Monitoring System
The Twitter Streamer is a Python application intended to notify cyber intelligence analysts or a specified audience of cyber threats found on Twitter, that target U.S. state, local, tribal, and territorial (SLTT) governments.


**History**

Research indicates cyber threat actors utilize social media platforms as well as personal blogs and websites to issue threats, claims of activity, or to communicate with other threat actors. Chris Cooley and Philippe Langlois determined through extensive research that Twitter is an incredibly popular platform used by cyber threat actors (other than Nation State/APTs) to share claims of activity targeting SLTT entities.

In early 2015, Chris began leading the development of a cyber focused toolkit that enables cyber intelligence analysts to find, search for, and quickly identify cyber threats to SLTT partners sourced from open source information. In mid-2015, Philippe joined the initiative dubbed "SpydrSec" and created a foundation for a tool built with the programming language Python, and the integration of the Twitter API, which focused on obtaining information from Twitter, what is currently believed to be the most popular social media platform cyber threat actors use. This tool, now known simply as the Twitter Streamer, autonomously searches for new threats to SLTT governments posted on Twitter on a 24/7 basis. 

Currently, Chris and Phil are collectively developing a front end for this application and have many more awesome ideas in store for future projects.


**How It Works**

Threats are detected through keyword, domain, and SLTT Twitter account monitoring via the Twitter API. Within seconds of a threat being posted to Twitter, an automated email notification containing intricate details of the post and the affiliated cyber threat actor is delivered to a specified recepient. These details include the platform the Tweet was created with, the unique account ID associated with the actor (which can be used to track down and actor if their screen name changes), geolocation of the tweet if available, and much more. The data is also stored in a .json file for analysts to reference at a later date.


**Why is this important?**

Before the release of the Twitter Streamer, cyber intelligence analysts needed to monitor individual Twitter accounts manually to find new threats to SLTT entities. In 2015, Chris manually monitored over 120 Twitter accounts daily, searching for cyber threat activity targeting SLTT entities. As of July 2016, the Twitter Streamer autonomously monitors for threat activity originating from nearly 200 Twitter accounts and this number grows weekly.
 
The implementation of the Twitter Streamer in any open source cyber threat intelligence program allows analysts to reduce the amount of time focused on conducting manual research on Twitter while the Twitter Streamer simultaneously increases the number of new threats discovered. The Twitter Streamer, based on the current configuration, on average analyzes 250,000 tweets, detecting over 200 potential threats, in a 24 hour time period. This is a significant achievement that previously would have been unobtainable without the use of automation.
 
While the number of potential threats discovered is minuscule compared to the number of tweets analyzed, this figure drives home the point that the amount of manual analysis that would have previously been required to find a potential threat is not an efficient or effective use of resources.
    
---

## Installation
Currently the operation of the Twitter Streamer must be done from the command line.
You must have the following to operate this application:

* Debian Linux (other linux kernals have not been tested - use at your own risk)
     * Windows compatibility is not available at this time. 
* [Internet Connection](http://www.speedtest.net/)
* [Intermediate Python Skills](https://www.codecademy.com/learn/python)
* [Twitter Development Account](https://dev.twitter.com/)
	* You will need to create a Twitter application in order to obtain API keys to use this program. 
	* https://apps.twitter.com/

**Dependencies**

_Keep in mind that basic user accounts will likely need `sudo` access to install dependencies._

* Tweepy
* [Gmail API](https://developers.google.com/gmail/api/quickstart/python) ( _to be removed in a later version_ )
     * To install the Gmail Python API Library:
     `pip install --upgrade google-api-python-client`
     * Check out other installation options [here](https://developers.google.com/api-client-library/python/start/installation)\
* Mozilla Firefox

(This section to be updated)

## How to operate
(This section to come)

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
<a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nd/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Twitter Streamer</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/Azlirn/Twitter-Streamer" property="cc:attributionName" rel="cc:attributionURL">Philippe Langlois and Chris Cooley</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>.

**Copyright (c) 2016 Philippe Langlois & Chris Cooley**

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

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**
