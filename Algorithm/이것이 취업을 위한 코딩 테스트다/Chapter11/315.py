m, n = list(map(int, input().split()))
data = list(map(int, input().split()))
count = 0

for x in range(len(data)):
    for y in range(x):
        if data[y] != data[x]:
            count += 1



print(count)