class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_buckets = [0, 0, 0]

        for c in nums:
            color_buckets[c] += 1

        j = 0

        for c in range(3):
            while color_buckets[c]:
                color_buckets[c] -= 1
                nums[j] = c
                j += 1
            