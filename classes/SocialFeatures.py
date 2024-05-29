from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import uuid
from datetime import datetime

class ChatMessages:
    def __init__(self, contact_points=['localhost'], port=9042, keyspace='social_feature'):
        self.cluster = Cluster(contact_points, port=port)
        self.session = self.cluster.connect(keyspace)
        self.table_name = 'chat_messages'

    def insert_message(self, chat_room_id, sender_id, receiver_id, message_content):
        message_id = uuid.uuid1()
        timestamp = datetime.utcnow()
        query = f"""
        INSERT INTO {self.table_name} (chat_room_id, message_id, sender_id, receiver_id, timestamp, message_content)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.session.execute(query, (chat_room_id, message_id, sender_id, receiver_id, timestamp, message_content))

    def get_messages(self, chat_room_id, limit=50):
        query = f"""
        SELECT * 
        FROM {self.table_name} 
        WHERE chat_room_id = %s ORDER BY message_id DESC LIMIT %s;
        """
        return self.session.execute(query, (chat_room_id, limit))

# Example usage:
#chat_messages = ChatMessages()
#chat_messages.insert_message(uuid.uuid4(), uuid.uuid4(), uuid.uuid4(), 'Hi!')
#chat_room_id = uuid.uuid4()
#for message in chat_messages.get_messages(chat_room_id):
#    print(message)



class GuildMembers:
    def __init__(self, contact_points=['localhost'], port=9042, keyspace='social_feature'):
        self.cluster = Cluster(contact_points, port=port)
        self.session = self.cluster.connect(keyspace)
        self.table_name = 'guild_members'

    def insert_member(self, guild_id, member_id, guild_name, creation_date, member_role, membership_start_date):
        query = f"""
        INSERT INTO {self.table_name} (guild_id, member_id, guild_name, creation_date, member_role, membership_start_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.session.execute(query, (guild_id, member_id, guild_name, creation_date, member_role, membership_start_date))

    def get_members(self, guild_id):
        query = f"""
        SELECT * 
        FROM {self.table_name} WHERE 
        guild_id = %s;
        """
        return self.session.execute(query, (guild_id,))

# Example usage:
#guild_members = GuildMembers()
#guild_members.insert_member(uuid.uuid4(), uuid.uuid4(), 'King', datetime.utcnow(), 'Leader', datetime.utcnow())
#guild_id = uuid.uuid4()
#for member in guild_members.get_members(guild_id):
#    print(member)
