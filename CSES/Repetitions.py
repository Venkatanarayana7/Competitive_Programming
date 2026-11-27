dna_str = input().strip()
max = 1
current = 1
for i in range(1, len(dna_str)):
    if dna_str[i] == dna_str[i-1]:
        current+= 1
        if current > max:
            max = current
    else:
        current=1

print(max)

