import db
import config


db1 = db.DB(passwd = config.dbpass)

db1.dumpall()

