class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_map = {}

        if len(s) != len(t):
            return False

        for char in s:
            chars_map[char] = chars_map[char] + 1 if char in chars_map else 1
        
        for char in t:
            if char not in chars_map or chars_map[char] == 0:
                return False
            
            chars_map[char] -= 1
        
        return True
        
