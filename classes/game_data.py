from cassandra_db import CassandraSingleton

class GameData:
    def __init__(self, game_id, name, game_type, current_state, world_layout_details):
        self.game_id = game_id
        self.name = name
        self.game_type = game_type
        self.current_state = current_state
        self.world_layout_details = world_layout_details
        self._cassandra = CassandraSingleton()

    @staticmethod
    def insert_game(self):
        cassandra = CassandraSingleton()
        query = f"""
        INSERT INTO game_data (game_id, name, type, current_state, world_layout_details)
        VALUES ({self.game_id}, '{self.name}', '{self.game_type}', '{self.current_state}', {self.word_layout_details})
        """
        cassandra.execute_query(query)


    @staticmethod
    def fetch_game(query):
        cassandra = CassandraSingleton()
        cassandra.execute_query(query)

    # Delete a game from the database
    @staticmethod
    def delete_game(game_type, game_id):
        cassandra = CassandraSingleton()
        query = f"""
        DELETE FROM game_data WHERE type='{game_type}' AND game_id={game_id}
        """
        cassandra.execute_query(query)

    def display_game_info(self):
        print(f"Game ID: {self.game_id}")
        print(f"Name: {self.name}")
        print(f"Type: {self.game_type}")
        print(f"Current State: {self.current_state}")
        print("World Layout Details:")
        for key, value in self.world_layout_details.items():
            print(f"  {key}: {value}")




