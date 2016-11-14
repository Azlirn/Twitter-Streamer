from sqlalchemy import *
from sqlalchemy import create_engine
import datetime


# Column('track_term_id', Integer(), primary_key=True),
# Column('track_term', String(55), unique=True, index=True),
# Column('reason_added', String(255)),
# Column('created_by', String(25), default='StreamerBot', nullable=False),
# Column('created_on', DateTime(), default=datetime.now()),
# Column('date_inactive', DateTime()),
# Column('active', Boolean(), default=True),
# Column('modified_by', String(), default='StreamerBot', nullable=False),
# Column('updated_on', DateTime(), default=datetime.now(), onupdate=datetime.now())



db = create_engine('sqlite:///streamerDB.db')
metadata = MetaData(db)
connection = db.connect()
track = Table('track', metadata, autoload=True)
s = select([track])
rp = connection.execute(s)

# pulling existing records from database
dbTrackTerms = []

print '[*] Loading current database track values...'

for record in rp:
    dbTrackTerms.append(record.track_term)

# opening track file
print '[*] Opening track file...'
trackfile = open('data/track.txt', 'r')

print '[*] Comparing Database values to track text file...'

itemcount = 0

# try to add new terms to the database
try:
    for term in trackfile:
        # strip all unnecessary characters from terms in track
        stripWhite = term.strip()
        stripNewLine = stripWhite.strip('\n')
        stripRLine = stripNewLine.strip('\r')
        newTerm = stripRLine.replace(',', '')

        # if the term is not in the database, add it
        if newTerm not in dbTrackTerms:
            itemcount = itemcount + 1
            systime = datetime.datetime.now()
            ins = track.insert().values(
                track_term = newTerm,
                reason_added = '14NOV2016 Update',
                created_by = 'StreamerBot',
                created_on = systime,
                active = True,
                modified_by ='StreamerBot'
            )

            # commit the changes
            result = connection.execute(ins)

except Exception as e:
    print "\n[!] Error Importing Track Term: %s" % e

print '\n[*] Import Complete...'
print '[*] Added %s new terms...' % itemcount