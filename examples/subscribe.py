import asyncio

from postgres_pubsub.pubsub import PostgresPubSub
import logging

log = logging.getLogger(__name__)
log.setLevel("DEBUG")


async def subscribe():
    pubsub = PostgresPubSub()
    pubsub.subscribe("my_channel")
    while True:
        message = await pubsub.receive()
        log.debug(f"{message=}")


if __name__ == "__main__":
    asyncio.run(subscribe())
