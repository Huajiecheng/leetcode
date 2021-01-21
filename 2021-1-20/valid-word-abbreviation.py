class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        temp = 0
        l = 0
        for i in abbr:
            if i.isdigit():
                if i == "0" and temp == 0:
                    return False
                temp = 10* temp + int(i)
            else:
                l += temp
                if l < len(word) and word[l] == i:                
                    temp = 0
                    l += 1
                else:
                    return False
        return l + temp == len(word)
                
            
        