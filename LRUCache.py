class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.memory = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.memory.remove(key)
            self.memory.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache.keys()) == self.capacity:
            if key in self.cache.keys():
                self.cache[key] = value
                if key in self.memory:
                    self.memory.remove(key)
                    self.memory.append(key)
                else:
                    self.memory.append(key)
            else:
                removed = self.memory.pop(0)
                del self.cache[removed]

                self.cache[key] = value
                self.memory.append(key)
        else:
            self.cache[key] = value
            if key in self.memory:
                self.memory.remove(key)
                self.memory.append(key)
            else:
                self.memory.append(key)