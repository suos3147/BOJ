# 문제 출처: https://www.acmicpc.net/problem/1002

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x1-x2)**2+(y1-y2)**2  # 두 점 사이의 거리 ^ 2
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1+r2 < d:
            print(0)
        elif r1+r2 == d:
            print(1)
        else:
            print(2)
