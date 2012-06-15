import db

db1 = db.DB(passwd = '')

res = db1.get_dbs_list()

print res
