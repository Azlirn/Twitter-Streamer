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
blacklist = Table('blacklist', metadata, autoload=True)
s = select([blacklist])
rp = connection.execute(s)

# pulling existing records from database
dbBlacklistTerms = []

print '[*] Loading current database blacklist values...'

for record in rp:
    dbBlacklistTerms.append(record.bl_term)

# opening blacklist file
print '[*] Opening blacklist file...'
blacklistFile = open('data/blacklist.txt', 'r')

print '[*] Comparing Database values to blacklist text file...'

itemcount = 0

# try to add new terms to the database
try:
    for term in blacklistFile:
        # strip all unnecessary characters from terms in blackli
        stripWhite = term.strip()
        stripNewLine = stripWhite.strip('\n')
        stripRLine = stripNewLine.strip('\r')
        newTerm = stripRLine.replace(',', '')

        # if the term is not in the database, add it
        if newTerm not in dbBlacklistTerms:
            itemcount = itemcount + 1
            systime = datetime.datetime.now()
            ins = blacklist.insert().values(
                bl_term = newTerm,
                reason_added = '28DEC2016 Update',
                created_by = 'StreamerBot',
                created_on = systime,
                active = True,
                modified_by ='StreamerBot'
            )

            # commit the changes
            result = connection.execute(ins)

except Exception as e:
    print "\n[!] Error Importing Blacklist Term: %s" % e

print '\n[*] Import Complete...'
print '[*] Added %s new blacklist terms...' % itemcount