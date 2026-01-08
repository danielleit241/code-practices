from collections import defaultdict

class Timemap:
    
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        
        left, right = 0, len(values) - 1
        
        if values[0][1] > timestamp:
            return ""
        if values[-1][1] <= timestamp:
            return values[-1][0]
        
        res = ""

        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res