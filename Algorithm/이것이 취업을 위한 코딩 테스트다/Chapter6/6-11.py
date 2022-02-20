n = int(input())
array = []

for i in range(n):
    data = input().split()

    array.append((data[0], data[1]))

array = sorted(array, key=lambda x: x[1])

for item in array:
    print(item[0], end=' ')
