def find_days(weights, c):
    count = 0
    temp = 0
    for weight in weights:
        if temp + weight > c:
            count += 1
            temp = weight
        else:
            temp += weight
    count += 1
    return count
            
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left+right)//2
            if find_days(weights, mid) <= D:
                right = mid
            else:
                left = mid + 1
        return left
                
        
        