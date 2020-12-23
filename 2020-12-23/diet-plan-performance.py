class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        count = 0
        T = sum(calories[:k])
        for i in range(len(calories) - k + 1):
            if i != 0:
                T = T - calories[i-1] + calories[i+k-1]
            if T < lower:
                count -= 1
            elif T > upper:
                count += 1
        return count