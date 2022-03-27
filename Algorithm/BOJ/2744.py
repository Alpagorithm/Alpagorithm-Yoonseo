s = input()

for c in s:
    if c <= 'Z':
        a = ord(c) - ord('A') + ord('a')
        print(chr(a), end='')
    else:
        a = ord(c) - ord('a') + ord('A')
        print(chr(a), end='')
