data = input()
temp = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    temp = max(temp+num, temp*num)

print(temp)