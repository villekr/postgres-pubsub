import asyncio
import time

from postgres_pubsub.pubsub import PostgresPubSub


async def publish():
    pubsub = PostgresPubSub()
    while True:
        pubsub.publish("my_channel", str(time.time()))
        await asyncio.sleep(2)


if __name__ == "__main__":
    asyncio.run(publish())
