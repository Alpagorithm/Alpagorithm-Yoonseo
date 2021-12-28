n = 6
lost = [2, 4]
reserve = [1, 3, 5]

set_lost = set(lost) - set(reserve)
set_reserve = set(reserve) - set(lost)

for i in set_reserve:
    if i - 1 in set_lost:
        set_lost.remove(i-1)
        continue

    if i + 1 in set_lost:
        set_lost.remove(i+1)
        continue

answer = n - len(set_lost)

print(answer)
