class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for s in word:
                arr[ord(s)-ord("a")] += 1
            hm[tuple(arr)].append(word)
        return hm.values()