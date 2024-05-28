from cassandra_db import CassandraSingleton
from cassandra.query import SimpleStatement

class GameAnalytics:
    
    @staticmethod
    def add_event(self, event_type, timestamp, event_data):
        cassandra = CassandraSingleton()
        data = {
            'event_type': event_type,
            'timestamp': timestamp,
            'event_data': event_data
        }
        
        cassandra.insert_data('game_analytics', data)

    @staticmethod
    def get_events(self, event_type, start_time, end_time):
        cassandra = CassandraSingleton()
        query = f"SELECT timestamp, event_data FROM game_analytics WHERE event_type={event_type} AND timestamp >= {start_time} AND timestamp <= {end_time}",
        return cassandra.execute_query(query)
