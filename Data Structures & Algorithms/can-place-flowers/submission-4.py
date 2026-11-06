class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l, m, r = -1, 0, 1
        counter = 0
        while r <= len(flowerbed):
            left_spot = 0 if l < 0 else flowerbed[l]
            mid_spot = flowerbed[m]
            right_spot = 0 if r == len(flowerbed) else flowerbed[r]
            if left_spot + mid_spot + right_spot == 0:
                flowerbed[m] = 1
                counter += 1
            l += 1
            m += 1
            r += 1

        return counter >= n
