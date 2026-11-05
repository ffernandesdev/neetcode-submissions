class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lettersMapping = {}

        for i in range(len(s)):
            if s[i] not in lettersMapping:
                lettersMapping[s[i]] = t[i]

        if len(lettersMapping) != len(set(lettersMapping.values())):
            return False

        for i in range(len(s)):
            if lettersMapping[s[i]] != t[i]:
                return False

        return True