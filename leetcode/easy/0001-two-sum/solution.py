class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in store:
                return [store[num2], i]
            store[num1] = i
        return []