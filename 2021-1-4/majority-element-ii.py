class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        v1 = None
        v2 = None
        c1 = 0
        c2 = 0
        result = []
        for num in nums:
            if c1 == 0 and (c2 == 0 or (c2 >0 and num != temp2)):
                c1 += 1
                temp1 = num
            elif c2 == 0 and num != temp1:
                c2 += 1
                temp2 = num
            else:
                if num == temp1:
                    c1 += 1
                elif num == temp2:
                    c2 += 1
                else:
                    c1 -= 1
                    c2 -= 1
        if c1 > 0:
            v1 = temp1
        if c2 > 0:
            v2 = temp2
        c1 = 0
        c2 = 0
        for num in nums:
            if num == temp1:
                c1 += 1
            elif num == temp2:
                c2 += 1
        if c1 > len(nums)//3:
            result.append(v1)
        if c2 > len(nums)//3:
            result.append(v2)
        return result
                
            

                    
        
        
        