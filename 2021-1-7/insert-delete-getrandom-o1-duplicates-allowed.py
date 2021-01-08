class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = []
        self.idx = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.count))
        self.count.append(val)
        return len(self.idx[val]) == 1
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]: 
            return False
        remove, last = self.idx[val].pop(), self.count[-1]
        self.count[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.count) - 1)
        self.count.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.count)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()