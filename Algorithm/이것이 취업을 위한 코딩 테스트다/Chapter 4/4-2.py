n = int(input())

xn, yn, zn = 0, 0, 0

for i in range(n+1):
    if str(i).find('3', 0, 2) >= 0:
        xn += 1

for i in range(60):
    if str(i).find('3', 0, 2) >= 0:
        print(i)
        yn += 1

zn = yn
print((n+1)*60*60-((n+1)-xn)*(60-yn)*(60-zn))