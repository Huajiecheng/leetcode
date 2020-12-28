class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        result = [0] * len(barcodes)
        count = Counter(barcodes)
        p = 0
        for k,v in count.most_common():
            while v>0:
                barcodes[p] = k
                v -= 1
                p += 2
                if p >= len(barcodes):
                    p = 1
        return barcodes