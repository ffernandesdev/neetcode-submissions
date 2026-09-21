class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSequence = 0
        currentSequence = 0

        for num in nums:
            if num == 1:
                currentSequence += 1
            else:
                maxSequence = max(currentSequence, maxSequence)
                currentSequence = 0
        
        return max(currentSequence, maxSequence)
            