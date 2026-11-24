from collections import defaultdict
class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        
        n = len(arr)
        sum_pairs = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                sum_pairs[arr[i]+arr[j]].append((i, j))
        
        for a in range(n):
            for b in range(a+1, n):
                target = arr[a] + arr[b]
                for c, d in sum_pairs[target]:
                    if (a < c or (a==c and b < d)) and len({a, b, c, d}) == 4:
                        return [a, b, c, d]
    
        return [-1, -1, -1, -1]