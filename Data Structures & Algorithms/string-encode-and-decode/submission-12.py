class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))+ "#" +word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            j = i + 1
            i = j + length
            res.append(s[j:i])
            j = i
        return res