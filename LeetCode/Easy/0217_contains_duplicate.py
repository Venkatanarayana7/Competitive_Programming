# Problem: 217. Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Approach: Hash Set 
# Time: O(n) | Space: O(n)

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for num in nums:
            if num in lookup:
                return True
            lookup.add(num)
        return False

solver = Solution()

list_nums = [1, 2, 4, 6, 10, 6]
result = solver.containsDuplicate(list_nums)
print(f"Result is: {result}.")