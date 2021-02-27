class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alex, lee = 0,0
        flag = 0
        while(len(piles) > 2):
            if (flag == 0):
                if(piles[0] > piles[-1]):
                    alex += piles[0]
                    piles.pop(0)
                else:
                    alex += piles[-1]
                    piles.pop()
                flag == 1
            else:
                if(piles[0] > piles[-1]):
                    lee += piles[0]
                    piles.pop(0)
                else:
                    lee += piles[-1]
                    piles.pop()
                flag == 0
        if alex>lee:
            return True
        return false
        