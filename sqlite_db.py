import sqlite3
import time

conn = sqlite3.connect('sqlite.db')


def db_exec(query):
    cur = conn.cursor()
    result = cur.execute(query)
    conn.commit()
    if result:
        return result.fetchall()


def create_db():
    db_exec('drop table if exists locked_cards')
    db_exec('''
        create table locked_cards (
            id integer primary key,
            hpan varchar(32) not null unique,
            lock_time integer not null)
    ''')

    lock_card('15345343234')
    time.sleep(1)
    lock_card('26567544534')
    time.sleep(1)
    lock_card('36456323423')


def lock_card(hpan):
    t = int(time.time())
    db_exec('insert into locked_cards (hpan, lock_time) values ({}, {})'.format(hpan, t))


def reset_locked_cards():
    t = int(time.time()) - 60
    db_exec('delete from locked_cards where lock_time < {}'.format(t))


if __name__ == '__main__':
    # create_db()
    reset_locked_cards()
    res = db_exec('select * from locked_cards')
    print(res)
    conn.close()
