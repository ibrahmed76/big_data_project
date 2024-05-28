import redis
import json

class PlayerStatistics:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def set_player_stat(self, player_id, stat_category, stat_name, value):
        key = f"player:{player_id}:stats"
        self.client.hset(key, f"{stat_category}:{stat_name}", value)

    def get_player_stat(self, player_id, stat_category, stat_name):
        key = f"player:{player_id}:stats"
        return self.client.hget(key, f"{stat_category}:{stat_name}")

    def get_all_player_stats(self, player_id):
        key = f"player:{player_id}:stats"
        return self.client.hgetall(key)
