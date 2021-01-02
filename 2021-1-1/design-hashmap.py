class ListNode:
    def __init__(self, key = None, value =  None):
        self.next = None
        self.key = key
        self.value = value
       
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 2000
        self.heads = [ListNode(-1, None) for i in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        head = self.heads[key%self.size]
        curr = head.next
        while curr != None:
            if curr.key == key:
                curr.value = value
                return None                
            curr = curr.next        
        newnode = ListNode(key,value)
        newnode.next = head.next
        head.next = newnode
            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        head = self.heads[key%self.size]
        curr = head.next
        while curr != None:
            if curr.key == key:
                return curr.value                
            curr = curr.next        
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        curr = self.heads[key%self.size]
        while curr.next != None:
            if curr.next.key == key:
                curr.next = curr.next.next
                return None                
            curr = curr.next
        

        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)