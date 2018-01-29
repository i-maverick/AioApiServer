from aiohttp import web
import json
import peewee

import views

db = peewee.SqliteDatabase('peewee.db')


def setup_router(self):
    self.router.add_get('/', handle)
    self.router.add_get('/tasks', views.task_list)
    self.router.add_get('/tasks/{id}', views.task)


async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj))


if __name__ == '__main__':
    app = web.Application()
    db.connect()
    setup_router(app)
    web.run_app(app, host='127.0.0.1', port=8080)
