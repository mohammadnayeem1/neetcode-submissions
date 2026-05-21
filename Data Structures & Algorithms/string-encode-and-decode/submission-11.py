4#neet4#code4#love4#you

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        while i < len(s):
            while s[i] != "#":
                i += 1
            size = int(s[j:i])
            j = i + 1
            i = j + size
            res.append(s[j:i])
            j = i
        return res
       
        
