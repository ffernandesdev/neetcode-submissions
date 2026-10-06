class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            prefix[i+1] = prefix[i] + n

        for i in range(len(nums)):
            leftSum = prefix[i]
            rightSum = prefix[len(prefix) - 1] - prefix[i + 1]

            if leftSum == rightSum:
                return i
        
        return -1