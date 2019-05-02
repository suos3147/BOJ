# 문제 출처: https://www.acmicpc.net/problem/1110

import sys
import time 

#시작 시간 체크
#start_time = time.time()

if __name__ == "__main__":
    cycle_count = 0
    result = -1

    #입력: N은 0보다 크거나 같고 99보다 작거나 같은 정수
    while 1:
        N = int(sys.stdin.readline())
        if N<0 or N>99:
            continue
        else:
            break

    first_num = N//10 #몫만 반환
    last_num = N%10
    
    while N != result:
        result = (last_num*10)+((first_num+last_num)%10)
        first_num = result//10
        last_num = result%10
        cycle_count += 1

    #출력: 순환 횟수
    print(cycle_count)



#실행시간 출력
#print("--- %s seconds ---"%(time.time()-start_time))