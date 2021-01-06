class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1]-arr[0])//len(arr)
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left+right)//2
            if arr[mid] == arr[0]+mid*diff:
                left = mid + 1
            else:
                right = mid
        return arr[left] - diff
                
        
        #return (arr[0]+arr[-1])*(len(arr)+1)//2 - sum(arr)
        