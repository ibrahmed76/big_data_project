from cassandra_db import CassandraSingleton
import uuid

class GameObjectData:
    @staticmethod
    def insert_game_object(object_type, position_x, position_y, position_z, attributes):
        cassandra = CassandraSingleton()
        object_id = uuid.uuid4()
        cassandra.execute_query("""
        INSERT INTO game_objects (object_id, object_type, position_x, position_y, position_z, attributes)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (object_id, object_type, position_x, position_y, position_z, attributes))

    @staticmethod
    def get_game_object(object_id):
        cassandra = CassandraSingleton()
        result = cassandra.execute_query("""
        SELECT * FROM game_objects WHERE object_id=%s
        """, (object_id,))
        
        return result.one()

# Example usage:
#game_data = GameObjectData(contact_points=['localhost'], port=9042, keyspace='game_data')
#object_id = game_data.insert_game_object("player", 1.0, 2.0, 3.0, {"health": "100"})
#game_object = game_data.get_game_object(object_id)
#print(game_object)
#game_data.close()
