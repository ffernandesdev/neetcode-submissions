class Solution:
    def minOperations(self, logs: List[str]) -> int:
        min_ops = 0

        for op in logs:
            if op == "../":
                if min_ops > 0:
                    min_ops -= 1 
            elif op == "./":
                continue
            else:
                min_ops += 1
        
        return min_ops