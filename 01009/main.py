# 문제 출처: https://www.acmicpc.net/problem/1009

if __name__ == "__main__":
    while 1:
        try:
            T = int(input()) # 테스트 케이스 개수
            if T > 1: 
                raise ValueError
            break
        except ValueError:
            continue
    a,b = input().split() # a는 컴퓨터 개수 b는 데이터 개수

