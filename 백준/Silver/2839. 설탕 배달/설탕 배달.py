import sys
n = int(sys.stdin.readline())
res = 0

while n >= 0:
    if n%5 == 0:
        res += n//5
        n %= 5
        print(res)
        break
    else:
        n -= 3
        res += 1
else:
    print(-1)