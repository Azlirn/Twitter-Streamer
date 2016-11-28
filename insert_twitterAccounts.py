from sqlalchemy import *
from sqlalchemy import create_engine
import datetime
from tqdm import tqdm
import csv

# media_accounts = Table('media_accounts', metadata,
#                        Column('media_account_id', Integer(), Sequence('media_id_seq'), primary_key=True),
#                        Column('account_id', ForeignKey('accounts.account_id')),
#                        Column('media_link', String(255), nullable=False, index=True),
#                        Column('media_id', Integer(), nullable=False, unique=True, index=True),
#                        Column('media_type', String(25), default="Twitter", nullable=False, index=True),
#                        Column('media_status', String(25), nullable=False),
#                        Column('date_last_active', DateTime()),
#                        Column('date_last_checked', DateTime(), default=datetime.now, onupdate=datetime.now()),
#                        Column('created_by', String(25), default='StreamerBot', nullable=False),
#                        Column('created_on', DateTime(), default=datetime.now()),
#                        Column('modified_by', String(), default='StreamerBot', nullable=False),
#                        Column('updated_on', DateTime(), default=datetime.now(), onupdate=datetime.now()),
#                        Column('send_to_streamer', Boolean(), default=False),
#                        Column('send_to_mentions', Boolean(), default=False),
#                        Column('date_inactive', DateTime()),
#                        Column('active', Boolean(), default=True)
#                        )

db = create_engine('sqlite:///streamerDB.db')
metadata = MetaData(db)
connection = db.connect()
maccounts = Table('media_accounts', metadata, autoload=True)

itemcount = 0

f = open('data/SLTT_TwitterAccounts.csv', 'rU')
reader = csv.reader(f)
next(reader, None)  # ignore the csv headers
data = list(reader)

mid = 0

try:
    for row in tqdm(data):

        systime = datetime.datetime.now()
        link = row[3]

        mid = mid + 1

        itemcount = itemcount + 1
        ins = maccounts.insert().values(

            media_link=link,
            media_id=mid,
            media_type="Twitter",
            media_status="Unknown",
            created_by='StreamerBot',
            created_on=systime,
            modified_by='StreamerBot',
            send_to_streamer=False,
            send_to_mentions=True,
            active=True
        )

        # commit the changes
        result = connection.execute(ins)


except Exception as e:
    print "\n[!] Error Importing Media Account: %s" % e

print '\n[*] Import Complete...'
print '[*] Added %s new accounts...' % itemcount
