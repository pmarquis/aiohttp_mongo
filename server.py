import aiohttp
from aiohttp import web
import asyncio

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def add_person(request):
    name = request.match_info.get('name')
    if not name:
        raise web.HTTPBadRequest('No name given')
    return web.Response(

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)
