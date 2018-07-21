import asyncio
import websockets
import datetime
import random
'''
async def crawl():
	#open socket

	async with websockets.connect("ws://127.0.0.1:8001") as websocket:
		#send data
		await websocket.send("Hello world!")

asyncio.get_event_loop().run_until_complete(
	crawl())
'''
def crawl():
	async def time(websocket, path):
		while True:
			now = datetime.datetime.utcnow().isoformat() + 'Z'
			await websocket.send(now)
			await asyncio.sleep(random.random() * 3)

	start_server = websockets.serve(time, 'https://mysterious-springs-48423.herokuapp.com/', 8002)

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()
