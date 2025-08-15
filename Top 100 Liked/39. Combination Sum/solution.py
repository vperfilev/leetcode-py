from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def back_track(elements: List[int], selected:List[int], rest_sum: int) -> None:
            if rest_sum == 0:
                result.append(selected[:])
                return

            if not elements or rest_sum < 0:
                return

            for i in range(len(elements)):
                selected.append(elements[i])
                back_track(elements[i:], selected, rest_sum - elements[i])
                selected.pop()

        back_track(candidates, [], target)
        return result