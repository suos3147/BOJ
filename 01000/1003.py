def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


T = int(input())  # 테스트 케이스 개수
result = [0, 0]

for i in range(T):
    n = int(input())
    if fibonacci(n) == 0:
        result[0] += 1
    elif fibonacci(n) == 1:
        result[1] += 1
    print("%d %d" % (result[0], result[1]))
