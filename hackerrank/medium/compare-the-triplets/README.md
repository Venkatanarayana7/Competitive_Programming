# Compare the Triplets

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from <em>1</em> to <em>100</em> for three categories: <em>problem clarity</em>, <em>originality</em>, and <em>difficulty</em>. 
  
The rating for Alice's challenge is the triplet <em>a = (a[0], a[1], a[2])</em>, and the rating for Bob's challenge is the triplet <em>b = (b[0], b[1], b[2])</em>.
  
The task is to calculate their comparison points by comparing each category:    
   
<ul>
<li> If <em>a[i] > b[i]</em>, then Alice is awarded <em>1</em> point. </li>
<li> If <em>a[i] &lt; b[i]</em>, then Bob is awarded <em>1</em> point. </li>
<li> If <em>a[i] = b[i]</em>, then neither person receives a point.</li>
</ul>
 
  
<strong>Example</strong>   
  
<em>a = [1, 2, 3]</em>  
<em>b = [3, 2, 1]</em>  
<br/ >  
<ul>
<li>For elements *0*, Bob is awarded a point because <em>a[0] &lt; b[0]</em>. </li> 
<li>For the equal elements <em>a[1]</em> and <em>b[1]</em>, no points are earned. </li> 
<li>Finally, for elements <em>2</em>, <em>a[2] > b[2]</em> so Alice receives a point. </li> 
</ul>
  
The return array is <em>[1, 1]</em> with Alice's score first and Bob's second.  
  
<strong>Function Description</strong>  
  
Complete the function <em>compareTriplets</em> with the following parameter(s):  
  

- <em>int a[3]</em>: Alice's challenge rating  
- <em>int b[3]</em>: Bob's challenge rating   

  
<strong>Returns</strong>  
  
- <em>int[2]</em>: the first element is Alice's score and the second is Bob's score

**Input Format**

The first line contains <em>3</em> space-separated integers, <em>a[0]</em>, <em>a[1]</em>, and <em>a[2]</em>, the respective values in triplet <em>a</em>.		
The second line contains <em>3</em> space-separated integers, <em>b[0]</em>, <em>b[1]</em>, and <em>b[2]</em>, the respective values in triplet <em>b</em>.

**Constraints**

   
<ul>
<li> <em>1 &le; a[i] &le; 100</em></li>
<li> <em>1 &le; b[i] &le; 100</em></li>
</ul>

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T13:16:16.733Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice, bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/compare-the-triplets/problem)