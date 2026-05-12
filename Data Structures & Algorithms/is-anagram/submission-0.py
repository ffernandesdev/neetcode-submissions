class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(s) != len(t):
            return False

        for char in s:
            freq[char] = freq[char] + 1 if char in freq else 1

        for char in t:
            if char in freq and freq[char] > 0:
                freq[char] -= 1
            else:
                return False

        return True