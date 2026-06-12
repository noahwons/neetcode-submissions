class TimeMap:

    def __init__(self):
        self.model = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.model:
            self.model[key] = [[value, timestamp]]
        else:
            self.model[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.model: return ""
        
        l = 0
        r = len(self.model[key]) - 1
        value = ""
        while l <= r:
            m = (l + r) // 2
            if self.model[key][m][1] <= timestamp: 
                value = self.model[key][m][0]
            
            if self.model[key][m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
        
        return value
