import uuid
from cassandra_db import CassandraSingleton

class PlayerData:
    def __init__(self):
        self._cassandra = CassandraSingleton()
    
    def checkWorking(self, player_name):
        query = """SELECT player_name
                   FROM player_data
                   WHERE player_name = %s
                """
        result = self._cassandra.execute_query(query, (player_name,))
        
        if result:
            row = result.one()
            if row:
                print(f'{player_name} added')
            else:
                print('error')
        else:
            print('error')

    def register(self, player_name, email, password, achievements, inventory, friend_list, profile_picture=None):
        self._cassandra.execute_query("""
        INSERT INTO player_data (player_id, player_name, player_email, password, profile_picture, achievements, inventory, friend_list)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (uuid.uuid4(), player_name, email, password, profile_picture, achievements, inventory, friend_list))
        print(f"Player {player_name} added with email {email}")
        self.checkWorking(player_name)
    
    def login(self, email, password):
        query = """SELECT password
                   FROM player_data
                   WHERE player_email = %s
                """
        result = self._cassandra.execute_query(query, (email,))
    
        if result:
            row = result.one()
            if row and row.password == password:
                print('Authentication successful')
                return True
            else:
                print('Authentication failed')
                return False
        else:
            print('Authentication failed')
            return False



# # Example of how to use the PlayerDatabase class
# if __name__ == '__main__':
#     db = PlayerData()
    
#     # test
#     player_name = 'JohnDoe'
#     email = 'john.doe@example.com'
#     password = 'securepassword'
#     achievements = ['First Blood', 'Sharp Shooter']
#     inventory = ['Sword', 'Shield']
#     friend_list = ['JaneDoe', 'BobSmith']

#     db.register(player_name, email, password, achievements, inventory, friend_list)
#     #test with wrong pass 
#     db.login(email,"ndnnd")
#     #test with right pass
#     db.login(email,password)
