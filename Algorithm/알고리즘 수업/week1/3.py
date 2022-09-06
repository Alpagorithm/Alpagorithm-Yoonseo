# 하노이 탑
import sys

# 옮기려는 원반의 개수
num = int(sys.stdin.readline())


def hanoi(n, p_from, p_to, p_mid):
    if n == 1:  # 원반이 1개이면 무조건 원반을 1번에서 3번으로 옮긴다.
        print(p_from, p_to)
        return

    hanoi(n - 1, p_from, p_mid, p_to)  # 1번 기둥의 n-1 개의 원반을 2번 기둥으로 옮긴다
    print(p_from, p_to)  # 1번 기둥에 남아 있는 가장 큰 원반을 3번 기둥으로 옮긴다
    hanoi(n - 1, p_mid, p_to, p_from)  # 2번 기둥의 n-1개의 원반을 3번 기둥으로 옮긴다


print(2 ** num - 1)  # 이동 횟수 = 2^num - 1
hanoi(num, 1, 3, 2)
