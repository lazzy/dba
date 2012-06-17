import db
import getpass
import MySQLdb
import sys

def passwordcheck():
	print "MySQL root password:"
	passwd = getpass.getpass(">")
	
	try:
		MySQLdb.connect(host='localhost', user='root', passwd=passwd, db='mysql')
		global db1
		db1 = db.DB(passwd = passwd)
		menu()
	except MySQLdb.Error:
		print "Wrong password, try again"
		passwordcheck()

def rmenu():
	print "Wish you continue?"
	choise = raw_input("(y/n)> ")
	if choise == ('y' or 'yes'):
		menu()
	elif choise == ('n' or 'no'):
		print "Bye"
		sys.exit()
	else:
		"Wrong choise. Please try again"
		rmenu()


def menu():
	print "Databases list: '1'\n" + "Dump database: '2'\n" + "Dump all databases: '3'\n" "Quit: 'q'\n" + "Make your choise:" 
	choise = raw_input("> ")
	action(choise)

def action(choise):
	
	if choise == '1':
		for db in db1.dbslist():
			print db 
		rmenu()

	elif choise == '2':
		print "Enter database name: "
		dbname = raw_input("> ")
		db1.dump(dbname)
		rmenu()

	elif choise == '3':
		db1.dumpall()
		rmenu()

	elif choise == 'q':
		print "Bye"
		sys.exit()

	else: 
		"Wrong choise. Please try again"
		menu()
	

print '-'*34 + '\n' + "-"*10 + "Welcome to DBA" + "-"*10 + '\n' + '-'*34
passwordcheck()
