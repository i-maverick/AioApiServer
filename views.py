import json
import peewee
import status
from aiohttp import web

import models


async def task_list(request):
    tasks = [{'id': t.id, 'title': t.title, 'datetime': t.datetime} for t in models.Task.select()]
    response_obj = {'tasks': tasks}
    return web.Response(text=json.dumps(response_obj), status=status.HTTP_200_OK)


async def task(request):
    try:
        task_id = request.match_info['id']
        t = models.Task.get(id=task_id)
        one_task = {'id': t.id, 'title': t.title, 'datetime': t.datetime}
        response_obj = {'task': one_task}
        return web.Response(text=json.dumps(response_obj), status=status.HTTP_200_OK)
    except peewee.DoesNotExist:
        return web.Response(text='Task does not exist', status=status.HTTP_404_NOT_FOUND)
