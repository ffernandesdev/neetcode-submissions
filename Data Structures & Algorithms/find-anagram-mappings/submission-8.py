class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        valuesToPos = {}
        res = [0] * len(nums1)

        for i, num in enumerate(nums2):
            valuesToPos[num] = i
        
        for i, num in enumerate(nums1):
            res[i] = valuesToPos[num]

        return res