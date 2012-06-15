import MySQLdb

class DB:
	def __init__(self, user='root', host='localhost', passwd='password', dbname='mysql'):
		self.user = user
		self.host = host
		self.passwd = passwd
		self.dbname = dbname

	def get_dbs_list(self):

		db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.dbname)	
		db.query('SELECT Db from mysql.db;')
		r = db.use_result()
		dblist = []
		while 1:
			rec = r.fetch_row()
			if not rec: break
			dblist.append(rec[0][0])

		return dblist

	def get_db_dump(self, dbname):
		pass


	def get_all_dbs(self):
		pass

