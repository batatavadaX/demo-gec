from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiohttp import ClientSession 

async def job():
    aio_session = ClientSession()
    host = os.environ.get("HOST")
    async with aio_session.get(host) as response:
        if response.status == 200:
            print("✅ online!"+ "\n" + "status code: 200")
        else:
            print("❌ offline!" + str(status))
    await aio_session.close()

scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=600)

scheduler.start()
