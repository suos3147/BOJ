import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline().rstrip())

    while 1:
        if T > 1000000:
            T = int(sys.stdin.readline().rstrip)
        else:
            break
    
    for i in range(T):
        a, b = map(int,sys.stdin.readline().split())
        result.append(a+b)

    for i in range(T):
        print(result[i])