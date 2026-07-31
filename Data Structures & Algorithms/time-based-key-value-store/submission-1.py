class TimeMap:

    def __init__(self):
        self.stringMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = [value, timestamp]
        temp = self.stringMap.get(key, [])
        temp.append(pair)
        self.stringMap[key] = temp

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stringMap:
            return ""
        possibleChoices = self.stringMap[key]
        L, R = 0, len(possibleChoices) - 1
        res = ""
        while L <= R: 
            mid = L + (R - L) // 2
            if possibleChoices[mid][1] <= timestamp:
                res = possibleChoices[mid][0]
                L = mid + 1
            elif possibleChoices[mid][1] > timestamp: 
                R = mid - 1
        return res
        
