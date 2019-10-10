"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
"""

result = [
    [1, 0],  # fibonacci(n) 0 출력 개수
    [0, 1]  # fibonacci(n) 1 출력 개수
]

for n in range(2, 41):
    result[0].append(result[0][n-1]+result[0][n-2])
    result[1].append(result[1][n-1]+result[1][n-2])

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    n = int(input())
    print('%d %d' % (result[0][n], result[1][n]))
