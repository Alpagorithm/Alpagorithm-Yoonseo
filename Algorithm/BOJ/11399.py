n = int(input())
arr = list(map(int, input().split()))

answer = 0
arr.sort()

for i in arr:
    answer += i * n
    n = n-1

print(answer)