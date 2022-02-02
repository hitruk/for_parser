
import psycopg2
from config import config

class DDL_DB:
   
    params = config()
    sql_table_name = ''' SELECT table_name FROM information_schema.tables 
              WHERE table_schema='public' 
              ORDER BY table_name '''

    def __init__(self):
        self.conn = psycopg2.connect(**self.params)
        self.cur = self.conn.cursor()
    
    def db_version(self):
        """ """
        sql = ''' SELECT version() '''
        try:
            self.cur.execute(sql)
            resp = self.cur.fetchone()[0]
            print(resp)
            self.cur.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
    #???
    def create_all_tables(self, commands):
        """ """
        try:
           for command in commands:
               self.cur.execute(command)
               self.cur.execute(self.sql_table_name)
           resp = self.cur.fetchall()
           for row in resp:
               table_name = row[0]
               print('Create table: ', table_name)
           self.conn.commit()
           self.cur.close()
        except(Exception,  psycopg2.DatabaseError) as error:
           print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def drop_all_tables(self):
        """ """
        try:
            self.cur.execute(self.sql_table_name)
            resp = self.cur.fetchall()
            for row in resp:
                print('Drop table: ' ,row[0])
                table_name = row[0]
                self.cur.execute(f"DROP TABLE {row[0]} CASCADE")
            self.conn.commit()
            self.cur.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

