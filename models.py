import peewee
from datetime import datetime

from api import db


class Task(peewee.Model):
    title = peewee.CharField()
    datetime = peewee.DateTimeField()

    class Meta:
        database: db


if __name__ == '__main__':
    db.connect()
    db.create_table(Task)
    for i in range(1, 11):
        Task.create(title='Task {}'.format(i), datetime=datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    db.close()
