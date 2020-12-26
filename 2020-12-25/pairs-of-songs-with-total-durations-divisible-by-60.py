class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = [0]* 60
        result = 0
        for item in time:
            remainder[item%60] += 1
        for i in range(0,31):
            if i == 0 or i == 30:
                result += int(remainder[i]*(remainder[i]-1)/2)
            else:
                result += remainder[i]*remainder[60-i]
        return result