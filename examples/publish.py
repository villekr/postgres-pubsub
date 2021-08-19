import asyncio
import time
import logging

from postgres_pubsub.pubsub import PostgresPubSub

log = logging.getLogger(__name__)
log.setLevel("DEBUG")


async def publish():
    pubsub = PostgresPubSub()
    while True:
        pubsub.publish("my_channel", str(time.time()))
        await asyncio.sleep(2)


if __name__ == "__main__":
    asyncio.run(publish())
