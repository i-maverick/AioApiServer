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
        task_id = request.query.get('id', 0)
        pswd = request.query.get('pass', None)
        print(pswd)
        t = models.Task.get(id=task_id)
        one_task = {'id': t.id, 'title': t.title, 'datetime': t.datetime}
        response_obj = {'task': one_task}
        return web.Response(text=json.dumps(response_obj), status=status.HTTP_200_OK)
    except peewee.DoesNotExist:
        return web.Response(text='Task does not exist', status=status.HTTP_404_NOT_FOUND)


async def card_list(request):
    cards = [{'id': c.id, 'title': c.title, 'datetime': c.datetime} for c in models.Card.select()]
    response_obj = {'cards': cards}
    return web.Response(text=json.dumps(response_obj), status=status.HTTP_200_OK)


async def card(request):
    try:
        card_id = request.match_info['id']
        c = models.Card.get(id=card_id)
        one_card = {'id': c.id, 'title': c.title, 'datetime': c.datetime}
        response_obj = {'card': one_card}
        return web.Response(text=json.dumps(response_obj), status=status.HTTP_200_OK)
    except peewee.DoesNotExist:
        return web.Response(text='Card does not exist', status=status.HTTP_404_NOT_FOUND)
