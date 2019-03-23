import traceback
import logging
from scripts import starter, notifier, twitter_setup
from importlib import reload


reload(starter)
reload(notifier)

# Activates the Streamer
def main():

    #Set up debug logging
    logging.basicConfig(filename="TwitterStreamer.log", level=logging.DEBUG, format='%(asctime)s %(message)s ')

    track = starter.get_track()

    starter.print_headers()

    starter.disabling_ssl_warning()

    # set up the stream
    twitterStream = twitter_setup.set_up_listener()
    notifier.scriptstart_notify()

    # Connect to the streamer with track
    try:
        print("[*] Filtering live Twitter stream by %s key terms..." % len(track))
        twitterStream.filter(track=track)

    except Exception as e:
        print(str(e))
        traceback.print_exc()
        twitterStream.disconnect()
        logging.warning("WARNING - System disconnect")
        notifier.error_notify(str(e), 'Streamer Error -- NO DATA AVAILABLE -- ')
        starter.restart_program()
        reload(main())


if __name__ == '__main__':
    main()
