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

