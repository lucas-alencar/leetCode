from typing import List

#https://leetcode.com/problems/two-sum/
class Solution:
    def TwoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for index, num in enumerate(nums):
            difference = target - num

            if difference in num_to_index:
                return [num_to_index[difference], index]
            else:
                num_to_index[num] = index

        raise Exception("Impossible solution")