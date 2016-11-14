from sqlalchemy import *
from sqlalchemy import create_engine

print "\nConnecting to database..."
db = create_engine('sqlite:///streamerDB.db')
connection = db.connect()
metadata = MetaData(db)
# users = Table('users', metadata, autoload=True)
# s = select([users])
# rp = connection.execute(s)


