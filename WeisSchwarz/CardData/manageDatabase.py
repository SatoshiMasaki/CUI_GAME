import sqlite3
from contextlib import closing
import time


def createDatabase():
    dbname = "CardInformation.db"
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''
                          create table card (id string, name string, card_type string, 
                          color string, level string, cost string,
                          trigger string, power string, soul string,
                          feature1 string, feature2 string,
                          effect string)
                          '''
        c.execute(create_table)
        conn.commit()


def insertDatabase(data: tuple):
    dbname = "CardInformation.db"
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        insert_data = '''
                          insert into card(id, name, card_type, color, level, cost, trigger, power, soul, 
                          feature1, feature2, effect) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                      '''
        print("-----------")
        print(data)
        print("-----------")
        time.sleep(4)
        c.execute(insert_data, data)
        conn.commit()


if __name__ == '__main__':
    dbname = "CardInformation.db"
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        for i in c.execute("select * from card"):
            print(i)
