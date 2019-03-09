from django.conf import settings

from haystack.backends.whoosh_backend import WhooshSearchBackend, WhooshEngine
from redis import StrictRedis
import redis_lock
from whoosh.qparser import QueryParser
from whoosh.index import EmptyIndexError

from .haystack_redis import RedisStorage as _RedisStorage

redis_conn = StrictRedis(host=settings.REDIS_CONFIG['host'],
                         port=settings.REDIS_CONFIG['port'],
                         db=settings.REDIS_DATABASES['whoosh']['db'])


class RedisStorage(_RedisStorage):
    """
    Override haystack_redis.RedisStorage lock method to handle concurrent
    access of redis backend
    """
    def lock(self, name):
        return redis_lock.Lock(redis_conn, name)


class RedisSearchBackend(WhooshSearchBackend):

    def setup(self):
        """
        Defers loading until needed.
        """
        from haystack import connections

        self.storage = RedisStorage(self.path)

        self.content_field_name, self.schema = self.build_schema(
            connections[
                self.connection_alias].get_unified_index().all_searchfields())
        self.parser = QueryParser(self.content_field_name, schema=self.schema)

        try:
            self.index = self.storage.open_index(schema=self.schema)
        except EmptyIndexError:
            self.index = self.storage.create_index(self.schema)

        self.setup_complete = True


class RedisEngine(WhooshEngine):
    backend = RedisSearchBackend
