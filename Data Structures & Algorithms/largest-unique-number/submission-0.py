class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        largest = -1
        for num in count:
            if num > largest and count[num] == 1:
                largest = num
        return largest


