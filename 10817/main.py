import sys

if __name__ == "__main__":
    a, b, c = map(int,sys.stdin.readline().split()) 

    inList = [a, b, c]
    inList.sort()

    print(inList[1])