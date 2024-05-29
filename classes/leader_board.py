import uuid
from datetime import datetime
from cassandra_db import CassandraSingleton

class LeaderboardData:
    
    @staticmethod
    def add_score( leaderboard_id, metric, player_id, score):
        cassndra = CassandraSingleton()
        timestamp = datetime.now()
        query = """
        INSERT INTO leaderboard (leaderboard_id, metric, player_id, score, timestamp)
        VALUES (%s, %s, %s, %s, %s)
        """
        cassndra.execute_query(query, (uuid.UUID(leaderboard_id), metric, uuid.UUID(player_id), score, timestamp))

    def get_leaderboard(leaderboard_id, metric, limit=10):
        cassandra = CassandraSingleton()
        query = """
        SELECT player_id, score, timestamp FROM leaderboard
        WHERE leaderboard_id = %s AND metric = %s
        LIMIT %s
        """
        rows = cassandra.execute_query(query, (uuid.UUID(leaderboard_id), metric, limit))
        return list(rows)
    
if __name__ == '__main__':
    player_id = str(uuid.uuid4())
    leaderboard_id = str(uuid.uuid4())
    LeaderboardData.add_score(leaderboard_id, 'points', player_id, 1500)
    print(LeaderboardData.get_leaderboard(leaderboard_id,'points'))

