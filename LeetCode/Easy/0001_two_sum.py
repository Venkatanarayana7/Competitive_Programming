# Problem: 1. Two Sum 
# Link: https://leetcode.com/problems/two-sum/description/
# Approach: Hash map for complement lookup
# Time: O(n) | Space: O(n)

from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i

        return []

solver = Solution()

numbers_list = [1, 3, 7, 4, 11]
target_value = 11

result = solver.twoSum(numbers_list, target_value)
print(f"Results are: {result}.")