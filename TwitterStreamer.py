#!usr/bin/env python

### Author: Philippe Langlois
### Co-Author & Maintainer: Chris Cooley

import traceback
import logging
from scripts import Twitter_Listner, starter, notifier, twitter_setup
import subprocess

reload(Twitter_Listner)
reload(starter)
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
off = '\033[0m'     # Text Reset


# Activates the Streamer
def main():
    #Intended fix for Gmail API error when running OSX
    subprocess.call(['bash', '-c', 'source ~/.bashrc'])

    #Set up debug logging
    logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s %(message)s ')

    track = starter.get_track()

    starter.print_headers()

    starter.disabling_ssl_warning()

    # set up the stream
    twitterStream = twitter_setup.set_up_listener()
    notifier.scriptstart_notify()

    # Connect to the streamer with track
    try:
        print " [*] Filtering live Twitter stream by %s key terms..." % len(track)
        twitterStream.filter(track=track)

    except Exception, e:
        print str(e)
        traceback.print_exc()
        twitterStream.disconnect()
        logging.warning("WARNING - System disconnect")
        notifier.error_notify("Twitter Streamer: Unknown Error", str(e), ' -- NO DATA AVAILABLE -- ')
        starter.restart_program()
        reload(main())


if __name__ == '__main__':
    main()
