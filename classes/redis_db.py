import redis

class RedisSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connect()
        return cls._instance

    def connect(self):
        self.redis_client = redis.Redis(host='localhost', port='6379', 
                                              password='', decode_responses=True)

    def set(self, key, value):
        self.redis_client.hset(key, value)

    def get(self, key, field):
        return self.redis_client.hget(key, field)
