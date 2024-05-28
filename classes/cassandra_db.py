from cassandra.cluster import Cluster

class CassandraSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connect()
        return cls._instance

    def connect(self):
        self.cluster = Cluster(['localhost'])  
        self.session = self.cluster.connect('game')

    def execute_query(self, query):
        return self.session.execute(query)
    
    def insert_data(self, table : str, data : map) -> None:
        # Construct the INSERT query dynamically based on the table and data
        query = f"INSERT INTO {table} ("

        columns = ", ".join(data.keys())
        values = ", ".join([f"'{value}'" for value in data.values()])
        query += f"{columns}) VALUES ({values});"
        
        self.execute_query(query)
