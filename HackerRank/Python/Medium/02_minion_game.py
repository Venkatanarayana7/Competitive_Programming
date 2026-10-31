def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] in vowels:
            kevin_score += (len_string - i)
        else:
            stuart_score += (len_string - i)
            
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}" )
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)