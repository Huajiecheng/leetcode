class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        top = False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if arr[i] > arr[i+1]:
                if i == 0 or i == (len(arr)-1):
                    return False                    
                else:
                    top = True
            elif arr[i] < arr[i+1]:
                if top:
                    return False
        return top