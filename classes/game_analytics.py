from cassandra_db import CassandraSingleton

class GameAnalytics:
    
    @staticmethod
    def add_event(event_type, timestamp, event_data):
        cassandra = CassandraSingleton()
        query = f"INSERT INTO game_analytics ("
        data = {
            'event_type': event_type,
            'timestamp': timestamp,
            'event_data': event_data
        }
    
        columns = ", ".join(data.keys())
        values = ", ".join([f"'{value}'" for value in data.values()])
        query += f"{columns}) VALUES ({values});"
        
        
        cassandra.execute_query(query)

    @staticmethod
    def get_events(event_type, start_time, end_time):
        cassandra = CassandraSingleton()
        query = f"SELECT timestamp, event_data FROM game_analytics WHERE event_type='{event_type}' AND timestamp >= '{start_time}' AND timestamp <= '{end_time}'"
        return cassandra.execute_query(query)


if __name__ in "__main__":
    GameAnalytics.add_event('player_behaviour', '2021-06-01T00:00:00Z', '{"player_id": 12345, "action": "jump", "location": "x:100, y:200"}')