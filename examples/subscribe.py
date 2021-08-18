import asyncio

from postgres_pubsub.pubsub import PostgresPubSub
import logging

log = logging.getLogger(__name__)
log.setLevel("DEBUG")


async def subscribe():
    log.debug("subscribe")
    pubsub = PostgresPubSub()
    log.debug(f"{pubsub=}")
    pubsub.subscribe("my_channel")
    log.debug("pubsub.subscribe")
    while True:
        message = await pubsub.receive()
        log.debug(f"{message=}")
        print(message)


if __name__ == "__main__":
    log.debug("__main__")
    asyncio.run(subscribe())
