from redis_db import RedisSingleton
import json
import time

class GameStateData:
    @staticmethod
    def set_player_location(player_id, x, y):
        redis = RedisSingleton()
        timestamp = int(time.time())
        redis.set_with_field(f"player:{player_id}:location", "x", x)
        redis.set_with_field(f"player:{player_id}:location", "y", y)
        redis.set_with_field(f"player:{player_id}:location", "timestamp", timestamp)

    @staticmethod
    def get_player_location(player_id):
        redis = RedisSingleton()
        return redis.get_all(f"player:{player_id}:location")
    
    @staticmethod
    def add_game_event(game_id, event_type, player_id, item_id=None, enemy_id=None):
        redis = RedisSingleton()
        event = {
            "event_type": event_type,
            "player_id": player_id,
            "item_id": item_id,
            "enemy_id": enemy_id,
            "timestamp": int(time.time())
        }
        redis.set(f"game:{game_id}:events", f"'{event}'")
    
    @staticmethod
    def get_game_events(game_id):
        redis = RedisSingleton()
        events = redis.get(f"game:{game_id}:events")
        return [json.loads(event) for event in events]

    @staticmethod
    def set_resource_availability(self, game_id, resource_id, quantity, x, y):
        redis = RedisSingleton()
        resource = {
            "quantity": quantity,
            "location": {"x": x, "y": y},
            "timestamp": int(time.time())
        }
        redis.hset(f"game:{game_id}:resources", resource_id, json.dumps(resource))

    @staticmethod
    def get_resource_availability(game_id, resource_id):
        redis = RedisSingleton()
        resource = redis.hget(f"game:{game_id}:resources", resource_id)
        return json.loads(resource) if resource else None
    


if __name__ == "__main__":
    redis = RedisSingleton()
    GameStateData.add_game_event('game123', 'item_pickup', 'player123', item_id='item789')
    # GameStateData.set_player_location(124, 50, 60)
    # print(GameStateData.get_player_location(124))
    print(GameStateData.get_game_events('game123'))
    
    