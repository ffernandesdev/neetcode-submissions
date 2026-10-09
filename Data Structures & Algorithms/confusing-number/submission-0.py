class Solution:
    def confusingNumber(self, n: int) -> bool:
        consufingNumbers = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }

        stringN = list(str(n))
        rotatedN = stringN.copy()
        i, j = 0, len(stringN) - 1
        while i <= j:
            if stringN[i] not in consufingNumbers or stringN[j] not in consufingNumbers:
                return False
            rotatedN[i], rotatedN[j], = consufingNumbers[rotatedN[j]], consufingNumbers[rotatedN[i]]
            i += 1
            j -= 1
        
        return stringN != rotatedN