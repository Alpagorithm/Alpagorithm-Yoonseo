
# 재귀
def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return factorial(n-1) + factorial(n-2)


print(factorial(int(input())))

# 반복
a = int(input())
result = 1

for item in range(1, a+1, 1):
    result *= item
print(result)