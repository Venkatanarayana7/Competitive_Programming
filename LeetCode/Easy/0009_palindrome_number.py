num = int(input())

if num < 0:
    print("false")
else:
    copy = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num //= 10

    if rev == copy:
        print("true")
    else:
        print("false")
