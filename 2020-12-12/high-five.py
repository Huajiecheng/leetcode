class Solution:
    def key_method(self, elem):
        return elem[0]*101+(100-elem[1])
    
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key = self.key_method)
        result = []
        current_id = 0
        current_ave = 0
        for i,item in enumerate(items):
            if current_id != item[0]:
                current_id = item[0]
                current_ave = 0
                for j in range(i,i+5):
                    current_ave += items[j][1]
                current_ave = int(current_ave/5)
                result.append([current_id, current_ave])            
        return result
        