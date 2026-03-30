class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            value, count = self.cache[key]
            self.cache[key] = (value, count + 1)
            return value
        return - 1       

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # Eviction subcase needed
            if len(self.cache) == self.capacity:
                victim = min(self.cache, key = lambda x: self.cache[x][1])
                del self.cache[victim]
            
            self.cache[key] = (value, 1)

        elif key in self.cache:
            _, count = self.cache[key]
            self.cache[key] = (value, count + 1)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)