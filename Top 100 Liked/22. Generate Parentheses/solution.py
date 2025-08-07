from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def back_track(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                back_track(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                back_track(current + ')', open_count, close_count + 1)

        back_track('', 0, 0)
        return result