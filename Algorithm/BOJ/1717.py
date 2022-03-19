import sys
sys.setrecursionlimit(1000000)

def find_parent(parent, x):
    if parent[x] != x:
         parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    team, a, b = map(int, sys.stdin.readline().split())
    if team == 0:
        union_parent(parent, a, b)
    elif team == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
