n = int(input())
data = list(map(int, input().split()))
data.sort()

answer = 1

for i in data:
    if answer < i:
        break
    answer += i
    print(answer)

print(answer)