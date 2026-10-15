class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k - 1
        min_ops = k
        
        while r < len(blocks):
            curr_window = 0
            for i in range(l, r + 1):
                if blocks[i] == "W":
                    curr_window += 1
            min_ops = min(min_ops, curr_window)
            l += 1
            r += 1
        
        return min_ops