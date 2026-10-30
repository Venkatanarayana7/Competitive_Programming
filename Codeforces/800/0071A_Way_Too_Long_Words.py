import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    out = []

    for w in lines[1:]:
        n = len(w)
        if n > 10:
            out.append(f"{w[0]}{n-2}{w[-1]}")
        else:
            out.append(w)
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()