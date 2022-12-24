import aiohttp
from aiohttp import web
import asyncio
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb', 27017)
db = client["app_database"]

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def add_person(request):
    name = request.match_info.get('name')
    print("add_person " + name)
    if not name:
        raise web.HTTPBadRequest('No name given')
    res = await db["persons"].insert_one({'name': name})    
    print(res)
    return web.Response(text="Added " + name)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle),
                web.get('/add_person/{name}', add_person)])

if __name__ == '__main__':
    web.run_app(app)
