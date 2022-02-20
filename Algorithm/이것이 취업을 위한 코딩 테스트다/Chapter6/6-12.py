n, k = map(int, input().split())
input_a = list(map(int, input().split()))
input_b = list(map(int, input().split()))

input_a.sort()
input_b.sort(reverse=True)

for i in range(k):
    if input_a[i] < input_b[i]:
        input_a[i], input_b[i] = input_b[i], input_a[i]
    else:
        break

print(sum(input_a))