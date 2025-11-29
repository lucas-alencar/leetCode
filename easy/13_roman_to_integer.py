
class Solution:
    symbol_to_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        result = 0

        for index, letter in enumerate(s):
            if ((index + 1) < len(s)) and self.symbol_to_value[letter] < self.symbol_to_value[s[index+1]]:
                result -= self.symbol_to_value[letter]
            else:
                result += self.symbol_to_value[letter]


        return result
