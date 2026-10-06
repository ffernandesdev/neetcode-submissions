class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix =[[] for _ in range(len(matrix))]

        for r in range(len(matrix)):
            total = 0
            for c in range(len(matrix[r])):
                total += matrix[r][c]
                self.prefix[r].append(total)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            leftSum = self.prefix[r][col1 - 1] if col1 - 1 >= 0 else 0
            rightSum = self.prefix[r][col2]
            total += (rightSum - leftSum)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)