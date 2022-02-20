n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for item in array:
    print(item, end = ' ')
