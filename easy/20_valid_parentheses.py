from typing import List

class Solution:
    brackets_rel = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    def isValid(self, s: str) -> bool:
        brackets: List[str] = []

        for char in s:
            if char in self.brackets_rel:
                if (len(brackets) == 0) or (self.brackets_rel[char] != brackets.pop()):
                    return False
            else:
                brackets.append(char)
        return brackets == []
