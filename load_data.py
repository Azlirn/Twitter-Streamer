from sqlalchemy import *
from sqlalchemy import create_engine

db = create_engine('sqlite:///streamerDB.db')
connection = db.connect()
metadata = MetaData(db)


# # users = Table('users', metadata, autoload=True)
# # s = select([users])
# # rp = connection.execute(s)
#
# dbUserNames = []
#
# def load_usernames():
#     for record in rp:
#         dbUserNames.append(record.username)
#     return dbUserNames


# This method loads track terms for the Twitter Streamer
def loadTrack():
    track = Table('track', metadata, autoload=True)
    s = select([track])
    rp = connection.execute(s)
    trackTerms = []
    for record in rp:
        track.append(str(record.track_term))
    return trackTerms


# This method loads blacklist terms for the Twitter Streamer
def loadBlacklist():
    blacklist = Table('blacklist', metadata, autoload=True)
    s = select([blacklist])
    rp = connection.execute(s)
    blacklistTerms = []
    for record in rp:
        blacklist.append(str(record.bl_term))
    return blacklistTerms


def loadSLTTDomains():
    domains = Table('domains', metadata, autoload=True)
    s = select([domains])
    rp = connection.execute(s)
    domainList = []
    for record in rp:
        domainList.append(str(record.domain))
    return domainList

def loadTwitterAccounts():
    mediaAccounts = Table('media_accounts', metadata, autoload=True)
    s = select([mediaAccounts])
    rp = connection.execute(s)

    twitterAccountIDs = []

    for record in rp:
        if record.media_type == 'Twitter':
            if record.send_to_streamer == True and record.media_status == 'Active':
                twitterAccountIDs.append(str(record.media_id))
    return twitterAccountIDs

