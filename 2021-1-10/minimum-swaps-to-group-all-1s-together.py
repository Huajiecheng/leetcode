class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count = sum(data)
        left, right = 0, count - 1
        result = sum(data[:count])
        temp = result
        while right != len(data) - 1:
            temp = temp - data[left] + data[right+1]
            result = max(temp,result)
            left += 1
            right += 1
        return count - result
                
            
            
        