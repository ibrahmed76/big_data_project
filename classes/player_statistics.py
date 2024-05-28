from redis_db import RedisSingleton
import json

class PlayerStatistics:
        
    @staticmethod
    def set_player_stat(self, player_id, stat_category, stat_name, value):
        redis = RedisSingleton()
        key = f"player:{player_id}:stats"
        field = f"{stat_category}:{stat_name}"
        
        return redis.set_with_field(key, field, value)

    @staticmethod
    def get_player_stat(self, player_id, stat_category, stat_name):
        redis = RedisSingleton()
        key = f"player:{player_id}:stats"
        field = f"{stat_category}:{stat_name}"
        
        return redis.get_with_field(key, field)
        

    @staticmethod
    def get_all_player_stats(self, player_id):
        redis = RedisSingleton()
        key = f"player:{player_id}:stats"
        
        return redis.get_all(key)
