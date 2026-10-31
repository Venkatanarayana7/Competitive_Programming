if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = max(arr)
    # the least score is greater than or equal to -100 from Constraints
    runner = -100
    
    for score in arr:
       if score > runner and score < max_val:
            runner = score
    print(runner) 
