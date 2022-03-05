import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())
array_m = list(map(int, sys.stdin.readline().split()))

array.sort()

for target in array_m:
    start = 0
    end = n-1
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            answer = 1
            break
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(answer)
