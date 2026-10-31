def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    
    for i in range(0, n, k):
        substring = string[i:i+k]
        
        result = []
        seen = set()
        
        for char in substring:
            if char not in seen:
                result.append(char)
                seen.add(char)
                
        print(''.join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)