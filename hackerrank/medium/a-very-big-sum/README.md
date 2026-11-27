# A Very Big Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In this challenge, you need to calculate and print the sum of elements in an array, considering that some integers may be very large.

**Function Description**

Complete the $aVeryBigSum$ function with the following parameter(s):

- $int\ ar[n]$: an array of integers  

**Return**

- $long$: the sum of the array elements

**Input Format** 

The first line of the input consists of an integer $n$.  
The next line contains $n$ space-separated integers contained in the array. 

**Output Format**

Return the integer sum of the elements in the array.

**Constraints**  
$1 \le n \le 10$  
$0 \le ar[i] \le 10^{10}$  

**Sample Input**  

    STDIN                                                   Function
    -----                                                   --------
    5                                                       arr[] size n = 5
    1000000001 1000000002 1000000003 1000000004 1000000005  arr[...]  
    

**Output**   
	
    5000000015

**Note:** 

The range of the 32-bit integer is $(-2^{31}) ~to~  (2^{31} -1)~ or~ [-2147483648,2147483647]$.   

When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.  

**Input Format**




**Constraints**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T13:22:06.231Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for i in range(ar_count):
        sum += ar[i]
    return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/a-very-big-sum/problem)