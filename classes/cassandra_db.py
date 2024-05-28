from cassandra.cluster import Cluster

class CassandraSingleton:
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
            self._instance.connect()
        return self._instance

    def connect(self):
        self.cluster = Cluster(['127.0.0.1'])  
        self.session = self.cluster.connect('game')

    def execute_query(self, query, values=None):
        return self.session.execute(query, values)
