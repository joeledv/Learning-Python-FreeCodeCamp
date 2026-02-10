class HashTable:
    def __init__(self):
        self.collection = dict()
    
    def hash(self, word):
        sum_val = 0
        for char in range(len(word)):
            sum_val += ord(word[char])
        return sum_val
    
    def add(self, key, value):
        hashed_key = self.hash(key)
        
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]

    def lookup(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        
        return None
