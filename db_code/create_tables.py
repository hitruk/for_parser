import psycopg2 
from config import config
from db_obj.db import  DDL_DB

def create_tables_db():
    """ """

    commands = (
        """
        CREATE TABLE parent (
            id serial,
            title text NOT NULL,
            path text NOT NULL,
            UNIQUE (title, path),
            PRIMARY KEY (id) 
        )
        """,
        """
        CREATE TABLE child (
            id serial,
            id_parent int,
            title text,
            path text,
            PRIMARY KEY (id),
            FOREIGN KEY (id_parent)
                REFERENCES  parent (id)
        )
        """,
        """
        CREATE TABLE grandchild (
            id serial,
            id_child int,
            title text,
            path text,
            UNIQUE (title, path),
            PRIMARY KEY (id),
            FOREIGN KEY (id_child)
                REFERENCES child (id)
        )
        """)

    db = DDL_DB()
    db.create_all_tables(commands)

if __name__ == '__main__':
    print('---start---')
    create_tables_db()
    print('---end---')
