class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        wordList = self.hm[key]
        l = 0
        r = len(wordList)-1
        res = ""
        while l<=r:
            mid = (l+r)//2
            val,time = wordList[mid]
            if timestamp >= time:
                res = wordList[mid][0]
                l = mid + 1
            elif timestamp < time:
                r = mid -1
        return res