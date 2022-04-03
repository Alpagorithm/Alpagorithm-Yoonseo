# 모든 모험가를 그룹에 넣을 필요는 없다
# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력
# 공포도가 X인 모함가는 반드시 X명 이상으로 구성한 그룹에 참여

# (현재 그룹에 포함되어 있는 모함가의 수 >= 현재 확인중인 공포도) 일때 그룹 결성
n = input()
data = list(map(int, input().split()))

data.sort()

result = 0
count = 0

for a in data:
    count += 1
    if count >= a:
        result += 1
        count = 0

print(result)
