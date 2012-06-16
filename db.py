import MySQLdb
import os
import config

class DB:
	def __init__(self, user='root', host='localhost', passwd='password', dbname='mysql'):
		self.user = user
		self.host = host
		self.passwd = passwd
		self.dbname = dbname

	def dbslist(self):

		db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.dbname)	
		db.query('SELECT Db from mysql.db;')
		r = db.use_result()
		dblist = []
		while 1:
			rec = r.fetch_row()
			if not rec: break
			dblist.append(rec[0][0])

		return dblist

	def dump(self, dbname):
		
		os.popen("mysqldump -u %s -p%s -h %s %s > %s.sql " % (self.user, self.passwd, self.host, dbname, dbname))

	def dumpall(self):
		
		db = DB(passwd = config.dbpass)

		for db in db.dbslist():

			os.popen("mysqldump -u %s -p%s -h %s %s > %s.sql " % (self.user, self.passwd, self.host, db, db))


