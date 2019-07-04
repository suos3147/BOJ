# 문제출저: https://www.acmicpc.net/problem/9012

def input_ps(number):
    while number != 0:
            ps = input()
            if len(ps) >= 2 and len(ps) <= 50:
                number -= 1
            else:
                return ps

if __name__ == "__main__":
    NUMBER = int(input())

    input_ps(NUMBER)