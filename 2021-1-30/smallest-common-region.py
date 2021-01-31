class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        count = {}
        for region in regions:
            parent = region[0]
            for child in region[1:]:
                count[child] = parent
        
        if region1 not in count:
            return region1
        if region2 not in count:
            return region2

        ancestors = set()
        while region1 in count:
            ancestors.add(region1)
            region1 = count[region1]
        
        while region2 not in ancestors and region2 in count:
            region2 = count[region2]
        
        return region2
        