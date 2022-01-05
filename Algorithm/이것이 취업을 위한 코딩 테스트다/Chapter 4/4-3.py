n = input()
x, y = ord(n[0])-ord('a') + 1, int(n[1])
print(x, y)
count = 0

locations = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for location in locations:
    print(x + location[0], y + location[1])
    if 1 <= x + location[0] <= 8 and 1 <= y + location[1] <= 8:
        count += 1

print(count)