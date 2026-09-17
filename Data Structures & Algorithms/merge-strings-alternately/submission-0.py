class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        smallest = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(0, smallest):
            res += word1[i] + word2[i]
        
        if len(word1) > smallest:
            res += word1[smallest:]
        elif len(word2) > smallest:
            res += word2[smallest:]

        return res