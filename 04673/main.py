# 문제 출처: https://www.acmicpc.net/problem/4673

self_number = set(range(1,10001))

def remove_not_self_number(n):
    remove_number = n
    for i in range(n):
        place_value = n%10
        remove_number += place_value
        n = n//10
    if remove_number < 10001:
        self_number.discard(remove_number)

def print_self_number():
    for i in self_number:
        print(i)

if __name__ == "__main__":

    for i in range(1,10001):
        remove_not_self_number(i)

    print_self_number()