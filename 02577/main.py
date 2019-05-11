# 문제 출처: https://www.acmicpc.net/problem/2577

if __name__ == "__main__":
    count = [0]*10
    
    A = int(input())
    B = int(input())
    C = int(input())

    result = list(str(A*B*C))

    for i in range(len(result)):
       for j in range(0,10):
           if result[i] == str(j):
               count[j] += 1
               break

    for i in range(0,10):
        print(count[i])