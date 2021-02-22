class Solution:
    def reachNumber(self, target: int) -> int:
        num = int(math.ceil(math.sqrt(2 * abs(target) + 1/4)-1/2))
        overshoot = num * (1 + num) // 2 - target
        if overshoot & 1 > 0:
            num += 1
            if num & 1 == 0:
                num += 1
        return num
        