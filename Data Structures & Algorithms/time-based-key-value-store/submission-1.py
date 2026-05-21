class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        wordList = self.hm[key]
        print(wordList)
        l = 0
        r = len(wordList)-1
        res = -1
        while l<=r:
            mid = (l+r)//2
            val,time = wordList[mid]
            if timestamp > time:
                res = mid
                l = mid + 1
            elif timestamp < time:
                r = mid -1
            else:
                return wordList[mid][0]
        return wordList[res][0] if res != -1 else ""