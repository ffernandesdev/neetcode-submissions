class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for op in operations:
            match op:
                case "+":
                    score.append(score[-1] + score[-2])
                case "D":
                    score.append(score[-1] * 2)
                case "C":
                    score.pop()
                case _:
                    score.append(int(op))

        res = 0

        for point in score:
            res += point

        return res