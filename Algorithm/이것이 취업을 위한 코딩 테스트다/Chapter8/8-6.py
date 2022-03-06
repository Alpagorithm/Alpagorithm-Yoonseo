import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))

d = [0] * (n+1)
d[1] = array[0]
d[2] = max(d[1], array[1])

for x in range(3, n+1):
    d[n] = max(d[n-1], d[n-2]+array[n-1])

print(d[n])