# 문제 출처: https://www.acmicpc.net/problem/4673

self_number = set(range(1,10001))

def remove_not_self_number(n):
    remove_number = n
    while n != 0:
        remove_number += n%10
        n = n//10
    self_number.discard(remove_number)

if __name__ == "__main__":

    for i in range(1,10001):
        remove_not_self_number(i)

    for i in self_number:
        print(i)