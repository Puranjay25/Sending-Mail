import MySQLdb

def connect():
	a=MySQLdb.connect(db="#",user="root",host="localhost",passwd="#")
	b=a.cursor()
	return a,b