from cassandra_db import CassandraSingleton
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import uuid
from datetime import datetime

class ChatMessages:
    @staticmethod
    def insert_message(chat_room_id, sender_id, receiver_id, message_content):
        cassandra = CassandraSingleton()
        message_id = uuid.uuid1()
        timestamp = datetime.now()
        query = """
        INSERT INTO chat_messages (chat_room_id, message_id, sender_id, receiver_id, timestamp, message_content)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cassandra.execute_query(query, (chat_room_id, message_id, sender_id, receiver_id, timestamp, message_content))

    @staticmethod
    def get_messages(chat_room_id, limit=50):
        cassandra = CassandraSingleton()
        query = """
        SELECT * 
        FROM chat_messages 
        WHERE chat_room_id = %s ORDER BY message_id DESC LIMIT %s;
        """
        return cassandra.execute_query(query, (chat_room_id, limit))

# Example usage:
if __name__ == '__main__':
    
    ChatMessages.insert_message(uuid.uuid4(), uuid.uuid4(), uuid.uuid4(), 'Hi!')
    chat_room_id = uuid.uuid4()
    for message in ChatMessages.get_messages(chat_room_id):
        print(message)



class GuildMembers:
    @staticmethod
    def insert_member(guild_id, member_id, guild_name, creation_date, member_role, membership_start_date):
        cassandra = CassandraSingleton()
        query = """
        INSERT INTO guild_members (guild_id, member_id, guild_name, creation_date, member_role, membership_start_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cassandra.execute_query(query, (guild_id, member_id, guild_name, creation_date, member_role, membership_start_date))

    @staticmethod
    def get_members(guild_id):
        cassandra = CassandraSingleton()
        query = """
        SELECT * 
        FROM guild_members WHERE 
        guild_id = %s;
        """
        return cassandra.execute_query(query, (guild_id,))

# Example usage:
# if __name__ == '__main__':
#     GuildMembers.insert_member(uuid.uuid4(), uuid.uuid4(), 'King', datetime.now(), 'Leader', datetime.now())
#     guild_id = uuid.uuid4()
#     for member in GuildMembers.get_members(guild_id):
#         print(member)
