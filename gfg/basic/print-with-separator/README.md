# Print With Separator

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two strings  **s1**  and  **s2**, and a separator symbol separator, print s1 and s2 with separator between them, followed by a new line.

 **Examples :** 

```
Input: s1 = "Hello", s2 = "World", separator = "@"
Output: Hello@World
Explanation: s1 and s2 are printed with the @ symbol in between.
```

```
Input: s1 = "Geeks", s2 = "For", separator = "-"
Output: Geeks-For
Explanation: s1 and s2 are printed with the - symbol in between.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T14:03:49.045Z  

```py
s1 = input()
s2 = input()
separator = input()

# code here
print(f"{s1}{separator}{s2}")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/print-with-separator/1)