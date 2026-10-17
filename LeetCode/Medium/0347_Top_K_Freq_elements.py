# Problem: 347. Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Approach: Dictionary count + sort keys by frequency
# Time: O(n log n) | Space: O(n)
# Status: solved on Oct 17, 2026

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1

        fe = sorted(freq.keys(), key = lambda x: freq[x], reverse=True)
        return fe[:k]