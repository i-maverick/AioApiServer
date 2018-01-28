from aiohttp import web
import json


async def task_list(request):
    response_obj = {'tasks': []}
    return web.Response(text=json.dumps(response_obj), status=200)
