from game_analytics import GameAnalytics
from player_statistics import PlayerStatistics
from game_data import GameData
from cassandra_db import CassandraSingleton
from redis_db import RedisSingleton

def main():
    print(PlayerStatistics.get_all_player_stats(1))
    
    

if __name__ == '__main__':
    main()