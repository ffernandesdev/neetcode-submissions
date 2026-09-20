class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        c = 0

        while l <= r:
            m = l + ((r - l) // 2)

            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                c = m
            else:
                return m
        
        return c