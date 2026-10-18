class TimeMap:

    def __init__(self):
        self.vault = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vault:
            self.vault[key] = []
        self.vault[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vault:
            return ""
        values = self.vault[key]
        if values[0][0] > timestamp:
            return ""
            
        l = 0
        r = len(values) - 1
        while l < r:
            m = l + (r - l)//2
            time, val = values[m]
            if time == timestamp:
                return val
            if time < timestamp:
                l = m + 1
            elif time > timestamp:
                r = m - 1
        if values[l][0] > timestamp:
            return values[l-1][-1]
        return values[l][-1]
        
'''
[2,3,5]
'''