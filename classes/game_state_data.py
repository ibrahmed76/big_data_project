from redis_db import RedisSingleton
import json
import time

class GameStateData:
    def __init__(self):
        self.redis = RedisSingleton()

    def set_player_location(self, player_id, x, y):
        redis = RedisSingleton()
        timestamp = int(time.time())
        self.redis.hmset(f"player:{player_id}:location", {"x": x, "y": y, "timestamp": timestamp})

    def get_player_location(self, player_id):
        redis = RedisSingleton()
        return self.redis.hgetall(f"player:{player_id}:location")
    
    def add_game_event(self, game_id, event_type, player_id, item_id=None, enemy_id=None):
        redis = RedisSingleton()
        event = {
            "event_type": event_type,
            "player_id": player_id,
            "item_id": item_id,
            "enemy_id": enemy_id,
            "timestamp": int(time.time())
        }
        self.redis.lpush(f"game:{game_id}:events", json.dumps(event))
    
    def get_game_events(self, game_id):
        redis = RedisSingleton()
        events = self.redis.lrange(f"game:{game_id}:events", 0, -1)
        return [json.loads(event) for event in events]

    def set_resource_availability(self, game_id, resource_id, quantity, x, y):
        redis = RedisSingleton()
        resource = {
            "quantity": quantity,
            "location": {"x": x, "y": y},
            "timestamp": int(time.time())
        }
        self.redis.hset(f"game:{game_id}:resources", resource_id, json.dumps(resource))

    def get_resource_availability(self, game_id, resource_id):
        redis = RedisSingleton()
        resource = self.redis.hget(f"game:{game_id}:resources", resource_id)
        return json.loads(resource) if resource else None
    


if __name__ == "__main__":
    game_state = GameStateData()

    game_state.add_game_event('game123', 'item_pickup', 'player123', item_id='item789')