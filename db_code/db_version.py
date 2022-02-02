
import psycopg2
from config import config
from db_obj.db import DDL_DB


def version_db():
    """ """
    db = DDL_DB()
    db.db_version()

if __name__ == "__main__":
    version_db()
