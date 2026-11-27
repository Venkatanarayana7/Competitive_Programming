# CHN15A - Rating 520

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef And Operators

Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.
Relational Operators are operators which check relationship between two values. Given two numerical values  **A**  and  **B**  you need to help chef in finding the relationship between them that is,

First one is greater than second or, First one is less than second or, First and second one are equal.

 

### Input

First line contains an integer  **T**, which denotes the number of testcases. Each of the  **T**  lines contain two integers  **A**  and  **B**.

### Output

For each line of input produce one line of output. This line contains any one of the relational operators
'<', '>', '='.

### Constraints

1 ≤  **T**  ≤ 10000 1 ≤  **A**,  **B**  ≤ 1000000001
### Sample 1:
Input
Output

```
3
10 20
20 10
10 10

```

```
<
>
=
```

### Explanation:

In this example 1 as 10 is lesser than 20

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T14:20:31.224Z  

```py
# cook your dish here
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        print("=")
    elif a > b:
        print(">")
    else:
        print("<")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHN15A)