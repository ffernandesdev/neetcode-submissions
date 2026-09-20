class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valueIndex = {}

        for i in range(0, len(nums)):
            if nums[i] in valueIndex and abs(i - valueIndex[nums[i]]) <= k:
                return True
            else:
                valueIndex[nums[i]] = i
        
        return False