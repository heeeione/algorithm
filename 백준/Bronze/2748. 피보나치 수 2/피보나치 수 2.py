import sys
n = int(sys.stdin.readline())
res = [0,1]
for i in range(2,n+1):
    res.append(res[i-2]+res[i-1])
print(res[n])