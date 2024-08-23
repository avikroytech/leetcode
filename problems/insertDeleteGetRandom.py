import random

class RandomizedSet:

    def __init__(self):
        self.set_map = {}
        self.set = []

    def insert(self, val: int) -> bool:
        if val not in self.set_map:
            self.set_map[val] = val
            self.set.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.set_map:
            self.set.remove(val)
            del self.set_map[val]
            return True

        return False

    def getRandom(self) -> int:
        randomIndex = random.randint(0,len(self.set)-1)

        return self.set[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()