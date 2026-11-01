import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    k = int(data[1])
    
    scores = [int(x) for x in data[2:2+n]]
    
    target_score = scores[k - 1]
    
    ans = 0
    for score in scores:
        if score >= target_score and score > 0:
            ans += 1
        else:
            break
            
    print(ans)

if __name__ == '__main__':
    main()
