class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniorsCount = 0
	
        for passanger in details:
            if int(passanger[11:13]) > 60:
                seniorsCount += 1

        return seniorsCount