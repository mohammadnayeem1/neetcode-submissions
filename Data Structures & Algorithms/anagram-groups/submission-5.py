class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for word in strs:
            store = [0] * 26
            for l in word:
                store[ord(l) - ord("a")] += 1
            hm[tuple(store)].append(word)
        return hm.values()