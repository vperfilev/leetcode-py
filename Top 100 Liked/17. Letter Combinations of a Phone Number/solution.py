from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_symbols = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }

        combinations = ['']

        for digit in digits:
            letters = digit_to_symbols[digit]

            new_combinations = []
            for prefix in combinations:
                for letter in letters:
                    new_combinations.append(prefix+letter)

            combinations = new_combinations

        return combinations