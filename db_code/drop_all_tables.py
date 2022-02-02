
import psycopg2 
from config import config
from db_obj.db import DDL_DB

def del_all_tables():
    """ """
    db = DDL_DB()
    db.drop_all_tables()

if __name__ == "__main__":
    print('---start---')
    del_all_tables()
    print('---end---')
