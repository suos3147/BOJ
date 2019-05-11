#문제출처: https://www.acmicpc.net/problem/2448

import sys

def print_star(n):
    star = ["  *   "," * *  ","***** "]
    for i in range(n):
        for j in range(i):
            sys.stdout.write(star[i])
        print()

if __name__ == "__main__":
    while 1:
        user_input = int(sys.stdin.readline())
        for i in range(11):
            if user_input == 3*2**i:
                break
        if user_input == 3*2**i:
            break
        
    print_star(user_input)