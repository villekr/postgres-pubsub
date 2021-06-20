import os
import asyncio

import psycopg2


class PostgresPubSub:
    def __init__(
        self,
        *,
        host: str = None,
        port: str = None,
        dbname: str = None,
        user: str = None,
        password: str = None,
    ):
        host = host or os.getenv("HOST")
        port = port or os.getenv("PORT")
        dbname = dbname or os.getenv("DBNAME")
        user = user or os.getenv("USER")
        password = password or os.getenv("PASSWORD")

        self.conn = psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password
        )
        self.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.queue: asyncio.Queue = None

    def subscribe(self, channel: str):
        cursor = self.conn.cursor()
        cursor.execute(f"LISTEN {channel};")
        loop = asyncio.get_event_loop()
        loop.add_reader(self.conn, self._callback)
        if self.queue is None:
            self.queue = asyncio.Queue()

    def publish(self, channel: str, message: str):
        stmt = f"NOTIFY {channel}, '{message}';"
        self.conn.cursor().execute(stmt)

    async def receive(self) -> str:
        return await self.queue.get()

    def _callback(self):
        self.conn.poll()
        for notify in self.conn.notifies:
            self.queue.put_nowait(notify.payload)
        self.conn.notifies.clear()
