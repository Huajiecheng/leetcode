class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.count:
            self.count[key].append((value,timestamp))
        else:
            self.count[key] = [(value,timestamp)]
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.count:
            left, right = 0, len(self.count[key]) - 1
            nums = self.count[key]    
            if nums[0][1] > timestamp:
                return "" 
            while left < right:
                mid = (left+right)//2
                if nums[mid][1] > timestamp:
                    right = mid
                else:
                    left = mid + 1
            if nums[left][1] <= timestamp:
                return nums[left][0]
            else:
                return nums[left-1][0]
        else:
            return ""
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)