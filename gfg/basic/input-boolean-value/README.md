# Input Boolean Value

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Take a boolean value  **a**  as an input. The program should display its numeric representation:

- 1 for "true"
- 0 for "false"

 **Examples:**  

```
Input: a = true
Output: 1
```

```
Input: a = false
Output: 0
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T14:10:22.447Z  

```py
# code here
a = input()
if a == "true":
    print(1, end="")
elif a == "false":
    print(0, end="")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/input-boolean-value/1)