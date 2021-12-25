# 입력
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# 정렬
arr.sort(reverse=True)

sum = 0

i = 0

while i < m:
    if (i+1) % (k+1) == 0 and i != 0:
        sum += arr[1]
        i = i + 1
    else:
        for z in range(k):
            sum += arr[0]
            i = i + 1

print(sum)