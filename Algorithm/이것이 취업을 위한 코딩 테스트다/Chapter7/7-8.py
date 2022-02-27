n, m = map(int, input().split())
items = list(map(int, input().split()))

items.sort()

end = items[n-1]

while end >= 0:
    sum = 0
    for item in items:
        if item - end > 0:
            sum += item - end

    if sum >= m:
        break
    end -= 1

print(end)