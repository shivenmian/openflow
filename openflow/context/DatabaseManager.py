from vlite import VLite

class DatabaseManager:
    def __init__(self, collection_name="openflow"):
        self.vdb = VLite(collection=collection_name)

    def add(self, message, metadata):
        self.vdb.add(message, metadata=metadata)

    def similarity_search(self, query, k=5):
        return self.vdb.similarity_search(query, k=k)
    
    def retrieve_by_query(self, query):
        return self.vdb.retrieve(query)
    
    def retrieve_by_metadata(self, metadata):
        return self.vdb.get(where=metadata)

