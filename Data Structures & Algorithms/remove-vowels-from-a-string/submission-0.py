class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {"a","e","i","o","u"}
        res = ""

        for c in s:
            if c not in vowels:
                res += c
        
        return res
