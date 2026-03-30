class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if key in self.hashset:
            return
        self.hashset.append(key)

    def remove(self, key: int) -> None:
        try:
            self.hashset.remove(key)
        except ValueError:
            pass

        

    def contains(self, key: int) -> bool:
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)