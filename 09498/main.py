import sys

if __name__ == "__main__":
    userScore = int(sys.stdin.readline())

    while 1:
        if userScore < 0 or userScore > 100:
            userScore = int(sys.stdin.readline())
        else:
            break
    
    if userScore >= 90:
        print("A")
    elif userScore >= 80:
        print("B")
    elif userScore >= 70:
        print("C")
    elif userScore >= 60:
        print("D")
    else:
        print("F")