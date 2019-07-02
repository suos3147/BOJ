#문제출처: https://www.acmicpc.net/problem/2448

import sys

def print_star(n):
    star = ["  *   "," * *  ","***** "]
    for i in range(0, n):
        for j in range(n//3):
            sys.stdout.write(star[i%3])
        print()

if __name__ == "__main__":
    while 1:
        user_input = int(sys.stdin.readline())
        for i in range(11):
            if user_input == 3*2**i:
                break
        if user_input == 3*2**i:
            break
        
    #미완료 
