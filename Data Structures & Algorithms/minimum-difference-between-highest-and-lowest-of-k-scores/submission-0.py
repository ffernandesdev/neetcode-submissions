class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        smallest_diff = float("inf")
        while r < len(nums):
            diff = nums[r] - nums[l]
            smallest_diff = min(smallest_diff, diff)
            l += 1
            r += 1
        return smallest_diff