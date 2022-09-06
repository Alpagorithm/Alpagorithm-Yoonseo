# 이진탐색 트리 제곱근
import sys

n = int(sys.stdin.readline())
low, high = 1, n

while low <= high:
    mid = (low + high) // 2
    if mid ** 2 <= n and (mid+1) ** 2:
        print(mid)
        break
    elif mid ** 2 < high:
        low = mid + 1
    else:
        high = mid - 1
