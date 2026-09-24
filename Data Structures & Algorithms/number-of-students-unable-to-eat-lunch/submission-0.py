class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        count = {
            0: 0,
            1: 0,
        }

        for s in students:
            if s > 0:
                count[1] += 1
            else:
                count[0] += 1
        
        for s in sandwiches:
            if count[s] > 0:
                res -= 1
                count[s] -= 1
            else:
                break
        
        return res