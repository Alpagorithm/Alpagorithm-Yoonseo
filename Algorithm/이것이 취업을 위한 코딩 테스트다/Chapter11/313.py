n = input()

data = [n[0]]

for i in range(len(n) - 1):
    if n[i] != n[i + 1]:
        data.append(n[i + 1])

result0 = 0
result1 = 0

for i in data:
    if i == "0":
        result0 += 1
    elif i == "1":
        result1 += 1

print(min(result0, result1))
