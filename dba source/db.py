import MySQLdb
import os

class DB:
	def __init__(self, user='root', host='localhost', passwd='password', dbname='mysql'):
		self.user = user
		self.host = host
		self.passwd = passwd
		self.dbname = dbname

	def dbslist(self):
		db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.dbname)	
		db.query('SHOW DATABASES;')
		r = db.use_result()
		dblist = []
		
		while 1:
			rec = r.fetch_row()
			if not rec: break
			dblist.append(rec[0][0])

		return dblist

	def dump(self, dbname):
		os.popen("mysqldump -u %s -p%s -h %s %s > %s.sql " % (self.user, self.passwd, self.host, dbname, dbname))
		print "(%s done...)" % (dbname)
	
	def dumpall(self):
		for db in self.dbslist():
			self.dump(db)
