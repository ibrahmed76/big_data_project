from cassandra_db import CassandraSingleton
from cassandra.query import SimpleStatement

class GameAnalytics:
    def __init__(self):
        self.cassandra = CassandraSingleton()

    def add_event(self, event_type, timestamp, event_data):
        query = "INSERT INTO game_analytics (event_type, timestamp, event_data) VALUES (%s, %s, %s)"
        data = {
            'event_type': event_type,
            'timestamp': timestamp,
            'event_data': event_data
        }
        
        self.cassandra.insert_data('game_analytics', data)

    def get_events(self, event_type, start_time, end_time):
        query = f"SELECT timestamp, event_data FROM game_analytics WHERE event_type={event_type} AND timestamp >= {start_time} AND timestamp <= {end_time}",
        return self.cassandra.execute_query(query)
