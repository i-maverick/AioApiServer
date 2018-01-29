import json
import status
from aiohttp import web

import models


async def task_list(request):
    tasks = [{'title': t.title, 'datetime': t.datetime} for t in models.Task.select()]
    response_obj = {'tasks': tasks}
    return web.Response(text=json.dumps(response_obj), status=status.HTTP_200_OK)
