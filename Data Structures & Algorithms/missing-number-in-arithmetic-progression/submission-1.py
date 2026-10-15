class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)

        # Get the difference `difference`.
        difference = (arr[-1] - arr[0]) // n

        # The expected element equals the starting element.
        expected = arr[0]

        for val in arr:
            # Return the expected value that doesn't match val.
            if val != expected:
                return expected

            # Next element will be expected element + `difference`.
            expected += difference

        return expected