class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        actualArraySize = len(nums)

        for i, num in enumerate(nums):
            if num == val:
                r = actualArraySize - 1
                while r >= i:
                    if nums[r] != val:
                        nums[i], nums[r] = nums[r], nums[i]
                        actualArraySize -= 1
                        break
                    actualArraySize -= 1
                    r -= 1
        
        return actualArraySize