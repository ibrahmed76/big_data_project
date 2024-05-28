from cassandra_db import CassandraSingleton
from redis_db import RedisSingleton

def main():
    # cassandra = CassandraSingleton()
    # query = "SELECT * FROM game_analytics;"
    # result = cassandra.execute_query(query)
    # for row in result:
    #     print(row)
        
    print("Start for redis")
    redis = RedisSingleton()
    print(redis.get('player:1:stats', 'combat:damage_dealt'))

if __name__ == '__main__':
    main()