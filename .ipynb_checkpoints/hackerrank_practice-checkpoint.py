def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase[:size]
    lines = []
    
    for i in range(size):
        s = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4*size-3, '-'))
    
    # CORRECTED: Print top half (excluding center) + center + bottom half
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)