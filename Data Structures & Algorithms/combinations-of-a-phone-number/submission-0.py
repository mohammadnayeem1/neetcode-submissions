class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = ""
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.helper(0, res,curr,digitToChar,digits)
        return res
        
    def helper(self, i, res,curr,digitToChar,digits):
        if i == len(digits):
            
            if curr != "":
                res.append(curr)
            return
        chars = digitToChar[digits[i]]
        for c in chars:
            curr += c
            self.helper(i+1,res,curr,digitToChar,digits)
            curr = curr[:len(curr)-1]
    
        
            
        