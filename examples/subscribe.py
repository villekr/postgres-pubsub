import asyncio

from postgres_pubsub.pubsub import PostgresPubSub


async def subscribe():
    pubsub = PostgresPubSub()
    pubsub.subscribe("my_channel")
    while True:
        message = await pubsub.receive()
        print(message)


if __name__ == "__main__":
    asyncio.run(subscribe())
