class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curr_comb = [], []
        self.total = 0

        def dfs(i):
            if self.total == target:
                combs.append(curr_comb.copy())
                return
            if i >= len(nums) or self.total > target:
                return

            curr_comb.append(nums[i])
            self.total += nums[i]
            dfs(i)
            
            curr_comb.pop()
            self.total -= nums[i]
            dfs(i + 1)
        
        dfs(0)
        return combs
