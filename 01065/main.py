# 문제 출처: https://www.acmicpc.net/problem/1065

import sys

if __name__ == "__main__":
    count = 0

    while 1:
        user_input = int(sys.stdin.readline())
        if(user_input > 0 and user_input < 1001):
            break

    for i in range(1, user_input+1):
        if i <= 99:
            count += 1
        else:
            place_value = []
            while i != 0:
                place_value.append(i%10)
                i = i//10
            if place_value[0]-place_value[1] == place_value[1]-place_value[2]:
                count += 1
    
    print(count)