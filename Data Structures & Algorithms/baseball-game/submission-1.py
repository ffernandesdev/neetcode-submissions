class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score, res = [], 0

        for op in operations:
            match op:
                case "+":
                    res += score[-1] + score[-2]
                    score.append(score[-1] + score[-2])
                case "D":
                    res += score[-1] * 2
                    score.append(score[-1] * 2)
                case "C":
                    res -= score[-1]
                    score.pop()
                case _:
                    res += int(op)
                    score.append(int(op))

        return res