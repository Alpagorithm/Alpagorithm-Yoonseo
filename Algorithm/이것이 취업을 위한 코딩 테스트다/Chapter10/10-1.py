# 특정 원소가 속한 집합을 찾아 특정 부모 노드를 반환한다.
def find_parent(parent, x): # parent : 부모 테이블, x : 노드
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x: # 현재 부모가 자기 자신이 아니라면 (= 루트가 아니라면)
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a) # 각각의 루트 번호를 찾기
    b = find_parent(parent, b)
    if a < b: # 작은 원소가 부모 노드
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화히기

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i # 모든 parent 테이블에 대해서 자기 자신을 넣음

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b) # a와 b 가 연결되어있다는 의미

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, 1), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')