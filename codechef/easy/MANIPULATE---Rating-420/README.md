# MANIPULATE - Rating 420

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Find Remainder

Write a program to find the remainder when an integer  **A**  is divided by an integer  **B**.

### Input

The first line contains an integer  **T**, the total number of test cases. Then  **T**  lines follow, each line contains two Integers  **A**  and  **B**.

### Output

For each test case, find the remainder when  **A**  is divided by  **B**, and display it in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ A,B ≤ 10000
### Sample 1:
Input
Output

```
3 
1 2
100 200
40 15
```

```
1
100
10
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T14:15:50.632Z  

```py
# cook your dish here
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a%b)
```

---

[View on CodeChef](https://www.codechef.com/problems/MANIPULATE)