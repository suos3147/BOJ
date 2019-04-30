# 문제 출처: https://www.acmicpc.net/problem/1110

import sys
import time

#시작 시간 체크
start_time = time.time()

if __name__ == "__main__":
    cycle_count = 0
    result = -1

    while 1:
        n = int(sys.stdin.readline())
        if n<0 or n>99:
            continue
        else:
            break

    first_num = n//10 #몫만 반환
    last_num = n%10
    
    while n != result:
        result = (last_num*10)+((first_num+last_num)%10)
        first_num = result//10
        last_num = result%10
        cycle_count += 1

    print(cycle_count)



#실행시간 출력
print("--- %s seconds ---"%(time.time()-start_time))