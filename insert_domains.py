from sqlalchemy import *
from sqlalchemy import create_engine
import datetime
from tqdm import tqdm


# domains = Table('domains', metadata,
#                 Column('domain_id', Integer(), Sequence('domain_id_seq'), primary_key=True),
#                 Column('domain', String(255), index=True),
#                 Column('domain_status', String(25), nullable=False),
#                 Column('date_last_checked', DateTime(), default=datetime.now, onupdate=datetime.now()),
#                 Column('created_by', String(25), default='StreamerBot', nullable=False),
#                 Column('created_on', DateTime(), default=datetime.now()),
#                 Column('active', Boolean(), default=True),
#                 Column('modified_by', String(), default='StreamerBot', nullable=False),
#                 Column('updated_on', DateTime(), default=datetime.now(), onupdate=datetime.now())
#                 )



db = create_engine('sqlite:///streamerDB.db')
metadata = MetaData(db)
connection = db.connect()
domains = Table('domains', metadata, autoload=True)
s = select([domains])
rp = connection.execute(s)

# pulling existing records from database
dbDomains = []

print '[*] Loading current database domain values...'

for record in rp:
    dbDomains.append(record.domain)

print '[*] Comparing Database values to track text file...'

itemcount = 0

domainFile = open('data/GOV_Domain_list.txt', 'r')

try:
    # strip all unnecessary characters from terms in track
    for domain in tqdm(domainFile):

        dom = domain.strip('\n').strip('\r').strip().lower()
        rmcomma = dom.replace(',', '')
        rmquote = rmcomma.replace('"', '')

        # if the term is not in the database, add it
        if rmquote not in dbDomains:
            systime = datetime.datetime.now()
            ins = domains.insert().values(
                domain = rmquote,
                domain_status = 'NOT CHECKED',
                date_last_checked = systime,
                created_by = 'StreamerBot',
                created_on = systime,
                active = True,
                modified_by = 'StreamerBot',
                updated_on = systime
            )
            # commit the changes
            result = connection.execute(ins)
            itemcount = itemcount + 1

except Exception as e:
    print "\n[!] Error Importing Domain: %s" % e


print '\n[*] Import Complete...'
print '[*] Added %s new domains...' % itemcount