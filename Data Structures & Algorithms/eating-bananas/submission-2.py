class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_speed = 0

        while l <= r:
            m = (r + l)  // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours > h:
                l = m + 1
            else:
                min_speed = m
                r = m - 1
        return min_speed