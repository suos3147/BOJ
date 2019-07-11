import sys

if __name__ == "__main__":
    n, x = map(int, sys.stdin.readline().split())
    listA = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        if listA[i] < x:
            sys.stdout.write(str(listA[i])+" ")