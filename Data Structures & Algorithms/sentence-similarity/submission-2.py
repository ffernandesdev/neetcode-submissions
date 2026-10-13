class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similarWords = set()

        for pair in similarPairs:
            similarWords.add((pair[0], pair[1]))
            similarWords.add((pair[1], pair[0]))

        for i in range(len(sentence1)):
            word1, word2 = sentence1[i], sentence2[i]

            if word1 != word2 and (word1, word2) not in similarWords:
                return False
        
        return True