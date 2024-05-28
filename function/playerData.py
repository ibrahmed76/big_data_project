import redis
import json 
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid


# Establish connection to cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

# Establish connection to Redis
r = redis.Redis(
    host='localhost',
    port='6379',
    password='',
    decode_responses=True
)

# Function to push a transaction for a player
def earn(player_id, amount):
    r.lpush(f'player_transactions:{player_id}', json.dumps({
        'timestamp': '.'.join(map(str, r.time())),
        'delta': amount
    }))


#check if cassandra is working
def checkWorking():
    session.execute("USE game;")
    rows = session.execute("SELECT * FROM player_profiles")
    for row in rows:
        print(row)

def register(player_name, level, experience_points, achievements, inventory):
    session.execute("USE game;")
    session.execute("""
        INSERT INTO player_profiles (player_id, player_name, level, experience_points, achievements, inventory)
        VALUES (%s, %s, %s, %s, %s, %s);""",
        (uuid.uuid4(), player_name, level, experience_points, achievements, inventory))

# Example function call to push a transaction
# earn(2, 30000)

# Retrieve and print the transactions for player 1
# transactions = r.lrange('player_transactions:2', 0, -1)
# for transaction in transactions:
#     transaction_data = json.loads(transaction)
#     print(f"Transaction - Timestamp: {transaction_data['timestamp']}, Amount: {transaction_data['delta']}")


register("joe",100,2000,['First Kill', 'Treasure Hunter'], ['Sword', 'Shield', 'Potion'])
checkWorking()

cluster.shutdown()