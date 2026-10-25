class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i = j = 0
        
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0' or abbr[j].isalpha():
                return False
            else:
                offset = ""
                while j < n and abbr[j].isdigit():
                    offset += abbr[j]
                    j += 1
                i += int(offset) if offset else 0
        return i == m and j == n