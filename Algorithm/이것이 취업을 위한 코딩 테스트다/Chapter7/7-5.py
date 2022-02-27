n = int(input())
n_items = list(map(int, input().split()))

m = int(input())
m_items = list(map(int, input().split()))

n_items.sort()

# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        print("no", end=" ")
        return None

    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        print("yes", end=" ")
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


for item in m_items:
    binary_search(n_items, item, 0, n-1)