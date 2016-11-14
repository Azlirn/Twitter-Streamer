from datetime import datetime
from sqlalchemy import create_engine, MetaData, DateTime, Table, Column, Integer, String, ForeignKey, Boolean, Sequence

metadata = MetaData()


# Create the table that will house the "parent" accounts for all media accounts in the database.
defaultAccountDesc = 'Limited information available regarding this account'
accounts = Table('accounts', metadata,
                 Column('account_id', Integer(), Sequence('account_id_seq'), primary_key=True),
                 Column('account_name', String(), nullable=False, unique=True, index=True),
                 Column('account_summary', String(255), default=defaultAccountDesc, nullable=False),
                 Column('created_by', String(25), default='StreamerBot', nullable=False),
                 Column('created_on', DateTime(), default=datetime.now()),
                 Column('modified_by', String(), default='StreamerBot', nullable=False),
                 Column('updated_on', DateTime(), default=datetime.now(), onupdate=datetime.now())
                 )

# Create the table that will hold the media accounts. This table is linked to the accounts table.
media_accounts = Table('media_accounts', metadata,
                       Column('media_account_id', Integer(), Sequence('media_id_seq'), primary_key=True),
                       Column('account_id', ForeignKey('accounts.account_id')),
                       Column('media_link', String(255), nullable=False, index=True),
                       Column('media_id', Integer(), nullable=False, unique=True, index=True),
                       Column('media_type', String(25), default="Twitter", nullable=False, index=True),
                       Column('media_status', String(25), nullable=False),
                       Column('date_last_active', DateTime()),
                       Column('date_last_checked', DateTime(), default=datetime.now, onupdate=datetime.now()),
                       Column('created_by', String(25), default='StreamerBot', nullable=False),
                       Column('created_on', DateTime(), default=datetime.now()),
                       Column('modified_by', String(), default='StreamerBot', nullable=False),
                       Column('updated_on', DateTime(), default=datetime.now(), onupdate=datetime.now()),
                       Column('send_to_streamer', Boolean(), default=False),
                       Column('send_to_mentions', Boolean(), default=False),
                       Column('date_inactive', DateTime()),
                       Column('active', Boolean(), default=True)
                       )

# Create the table used for the streamer track.
track = Table('track', metadata,
              Column('track_term_id', Integer(), Sequence('track_id_seq'), primary_key=True),
              Column('track_term', String(55), unique=True, index=True),
              Column('reason_added', String(255)),
              Column('created_by', String(25), default='StreamerBot', nullable=False),
              Column('created_on', DateTime(), default=datetime.now()),
              Column('date_inactive', DateTime()),
              Column('active', Boolean(), default=True),
              Column('modified_by', String(), default='StreamerBot', nullable=False),
              Column('updated_on', DateTime(), default=datetime.now(), onupdate=datetime.now())
              )

# Create the table used for the streamer blacklist.
blacklist = Table('blacklist', metadata,
                  Column('bl_term_id', Integer(), Sequence('blacklist_id_seq'), primary_key=True),
                  Column('bl_term', String(55), unique=True, index=True),
                  Column('reason_added', String(255)),
                  Column('created_by', String(25), default='StreamerBot', nullable=False),
                  Column('created_on', DateTime(), default=datetime.now()),
                  Column('date_inactive', DateTime()),
                  Column('active', Boolean(), default=True),
                  Column('modified_by', String(), default='StreamerBot', nullable=False),
                  Column('updated_on', DateTime(), default=datetime.now(), onupdate=datetime.now())
                  )

domains = Table('domains', metadata,
                Column('domain_id', Integer(), Sequence('domain_id_seq'), primary_key=True),
                Column('domain', String(255), index=True),
                Column('domain_status', String(25), nullable=False),
                Column('date_last_checked', DateTime(), default=datetime.now, onupdate=datetime.now()),
                Column('created_by', String(25), default='StreamerBot', nullable=False),
                Column('created_on', DateTime(), default=datetime.now()),
                Column('active', Boolean(), default=True),
                Column('modified_by', String(), default='StreamerBot', nullable=False),
                Column('updated_on', DateTime(), default=datetime.now(), onupdate=datetime.now())
                )

engine = create_engine('sqlite:///streamerDB.db')
metadata.create_all(engine)

print "[*] Database creation complete!"