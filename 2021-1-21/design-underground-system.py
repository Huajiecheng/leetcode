class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.time = defaultdict(lambda:[0,0])
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)
               

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        record = self.customer.pop(id)
        self.time[record[0]+'-'+stationName][0] += (t - record[1])
        self.time[record[0]+'-'+stationName][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float: 
        record  = self.time[startStation+'-'+endStation]
        return record[0]/record[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)