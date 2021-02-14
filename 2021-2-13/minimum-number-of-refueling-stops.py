class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        current,stations,heap,stops = startFuel,stations[::-1],[],0
        while current < target:
            while stations and stations[-1][0] <= current:
                heapq.heappush(heap,-stations.pop()[1])
            if not heap and current < target :
                return -1
            check = stations[-1][0] if stations else target
            while heap and current < check:
                current += -heapq.heappop(heap)
                stops += 1
        return stops
        