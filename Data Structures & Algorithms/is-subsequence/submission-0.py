class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s can never be a subsequence of t if its length is bigger
        if len(s) > len(t):
            return False
        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)