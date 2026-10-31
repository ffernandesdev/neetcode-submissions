class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
          ")": "(",
          "]": "[",
          "}": "{", 
        }
        stack = []

        for bracket in s:
            if bracket not in closeToOpen:
                stack.append(bracket)
            else:
                openBracket = closeToOpen[bracket]
                if not stack or openBracket != stack.pop():
                    return False

        return len(stack) == 0
