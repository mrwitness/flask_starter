#! /usr/bin/env python
#coding=utf-8
import psycopg2
import time

class PostgresDB:
    def __init__(self,host,port,user,password,dbname):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.dbname=dbname
	self.connected=False

    def connect(self):
	if self.connected:
          return True
        tryTime = 3
        while not self.connected and tryTime > 0:
         try:
           tryTime = tryTime - 1
           self.connection = psycopg2.connect(connect_timeout=3,database=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
           self.connected = True
         except psycopg2.Error,e:
           print "psycopg2 Error %s" %str(e)
           time.sleep(1)
        if self.connected == False:
          print "Connecte to DB %s Failed..."%self.dbname
          return self.connected
        else:
          self.cursor=self.connection.cursor()
          return self.connected

    def disconnect(self):
	if self.connected:
		self.connection.commit()
		self.connection.close()

    def sqlquery(self,sql):
	if not self.connected:
		print 'database is not connected,connect first'
		return False
        self.cursor.execute(sql)
        return True

    def get_all_tables(self):
 	getTable = "SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'"
	ret = self.sqlquery(getTable)
	if ret == False:
		return []
 	allTables = self.cursor.fetchall()	
	list = []
	for table in allTables:
		list.append(table[0]+"."+table[1])
	return list
   
    def get_columns_names_of_table(self,table):
	sql = "Select * FROM %s limit 1"%table
	self.cursor.execute(sql)
	return [desc[0] for desc in self.cursor.description]

    def get_columns_types_of_table(self,table):
	sql = "Select * FROM %s limit 1"%table
	self.cursor.execute(sql)
	return [desc[1] for desc in self.cursor.description]

    def get_columns_of(self,tablename):
	if self.connected == False:
		return []
	table = tablename 	#format tablename if need
	sql = "Select * FROM %s limit 1"%table
	self.cursor.execute(sql)
	list = []
	names = [desc[0] for desc in self.cursor.description]
	types = [desc[1] for desc in self.cursor.description]
	list.append(names)
	list.append(types)
	return list
 
    # return -1:error
    def get_count_of(self,tablename):
	if self.connected == False:
		return -1
	sql = "Select count(*) FROM %s"%tablename
	ret = self.sqlquery(sql)
	if ret==False:
		return -1
	list = self.cursor.fetchall()
	return list[0][0]

    def get_column_number_of(self,tablename):
	if self.connected == False:
		return -1
	return len((self.get_columns_of(tablename))[0])

    def select_all_from(self,tablename):
	return self.select_all_from(tablename,"")

    def select_all_from(self,tablename,whereClouser):
	if self.connected == False:
		return []
	sql = "select * from %s %s"%(tablename,whereClouser)
	ret = self.sqlquery(sql)
	if ret == False:
		return []
	return self.cursor.fetchall()




