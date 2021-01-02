class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.count:
            return False         
        else:
            self.count[val] = len(self.list)
            self.list.append(val)
            return True
            
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.count:
            index = self.count[val] 
            self.list[index] = self.list[-1]
            self.count[self.list[index]] = index
            self.list.pop()
            self.count.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()