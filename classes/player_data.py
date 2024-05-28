import redis

class Player:
    def __init__(self, player_id=None, username=None, email=None, profile_picture=None, achievements=None, inventory=None, friend_list=None):
        self.redis = redis_client
        self.player_id = player_id
        self.username = username
        self.email = email
        self.profile_picture = profile_picture
        self.achievements = achievements or []
        self.inventory = inventory or []
        self.friend_list = friend_list or []

    def save(self):
        pass

    def load(self):
        pass

    def delete(self):
        pass

# Usage example:
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
player = Player(redis_client, username="player1", email="player1@example.com")
player.save()
