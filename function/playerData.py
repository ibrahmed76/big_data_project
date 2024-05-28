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



#check if cassandra is working
def checkWorking(player_name):
    session.execute("USE game;")
    query = """SELECT player_name
               FROM player_profiles
               WHERE player_name = %s
               """
    result = session.execute(query, (player_name,))
    
    # Check if the result contains any rows
    if result:
        # Fetch the first row from the result
        row = result.one()
        if row:
            print(f'{player_name} added')
        else:
            print('error')
    else:
        print('error')

def register(player_name, email,password, achievements, inventory,inventory_list,friend_list, profile_picture=None):
    session.execute("USE game;")
    session.execute("""
    INSERT INTO player_data (player_id, player_name, player_email, password, profile_picture, achievements, inventory, friend_list)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (uuid.uuid4(), player_name, email, password, profile_picture, achievements, inventory, friend_list))
    print(f"Player {player_name} added with email {email}")
    checkWorking(player_name)

def login(player_name):
    session.execute("USE game;")
    query = """
"""



cluster.shutdown()