from cassandra.cluster import Cluster
import uuid

class GameObjectData:
    def __init__(self, contact_points=['localhost'], port=9042, keyspace='game_data'):
        self.cluster = Cluster(contact_points, port=port)
        self.session = self.cluster.connect()
        self.session.set_keyspace(keyspace)
        
    def insert_game_object(self, object_type, position_x, position_y, position_z, attributes):
        object_id = uuid.uuid4()
        self.session.execute("""
        INSERT INTO game_objects (object_id, object_type, position_x, position_y, position_z, attributes)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (object_id, object_type, position_x, position_y, position_z, attributes))
        return object_id

    def get_game_object(self, object_id):
        result = self.session.execute("""
        SELECT * FROM game_objects WHERE object_id=%s
        """, (object_id,))
        return result.one()

    def close(self):
        self.cluster.shutdown()

# Example usage:
#game_data = GameObjectData(contact_points=['localhost'], port=9042, keyspace='game_data')
#object_id = game_data.insert_game_object("player", 1.0, 2.0, 3.0, {"health": "100"})
#game_object = game_data.get_game_object(object_id)
#print(game_object)
#game_data.close()
