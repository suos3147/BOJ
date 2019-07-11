if __name__ == "__main__":
    n = int(input())
    
    while 1:
        if n<1 or n>10000:
            n = int(input())
        else:
            break

    result = 0
    
    for i in range(1,n+1):
        result += i

    print(total)