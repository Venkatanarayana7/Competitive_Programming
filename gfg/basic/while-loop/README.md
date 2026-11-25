# While Loop

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number  **n**, print all numbers from 0 to n in increasing order in a single line using a while loop.

 **Examples:** 

```
Input: n = 3
Output: 0 1 2 3
Explanation: Numbers from 0 to 3 in increasing order are 0 1 2 3.
```

```
Input: n = 5
Output: 0 1 2 3 4 5
Explanation: Numbers from 0 to 5 in increasing order are 0 1 2 3 4 5.
```

## Solution

**Language:** c(gcc5.4)  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-25T16:36:46.312Z  

```c(gcc5.4)
#include <stdio.h>

int main() {
    int i, n;
    scanf("%d", &n);
    
    for(i=0; i<n; i++){
        printf("%d ", i);
    }  
    printf("%d", n);
    return 0;
}
    


```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/while-loop/1)