class Solution:
    # nums = [1, 2, 1, 4], l = 4
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # [0, 0, 0, 0, 0, 0, 0, 0]
        ans = [0 for i in range(len(nums) * 2)]
        i = 0

        for j in range(len(nums), len(ans)):
            ans[i] = nums[i]
            ans[j] = nums[i]
            i += 1
        
        return ans