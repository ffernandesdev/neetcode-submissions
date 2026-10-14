class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            while nums[l] % 2 == 0 and l < r:
                l += 1
            while nums[r] % 2 != 0 and r > l:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums