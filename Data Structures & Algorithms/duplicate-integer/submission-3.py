class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        ht = dict()

        for i in range(0, n):
            key = f'{nums[i]}'
            if ht.get(key):
                return True
            ht[key] = True
        
        return False