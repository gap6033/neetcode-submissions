class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        values = self.storage[key]
        if values[0][0] > timestamp:
            return ""
        
        l = 0
        r = len(values) - 1
        while l <= r:
            m = l + (r - l)//2
            prev_timestamp = values[m][0]
            if prev_timestamp == timestamp:
                return values[m][-1]
            elif prev_timestamp > timestamp:
                r = m - 1
            elif prev_timestamp < timestamp:
                l = m + 1
        if values[m][0] > timestamp:
            return values[m-1][-1]
        return values[m][-1]
        

"""
alice: [(1, happy), (3, sad), (5, sad)]


"""