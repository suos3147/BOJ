if __name__ == "__main__":
    result = 0
    
    n = int(input()) # 숫자의 개수 입력

    while 1:
        if(n<1 or n>100):
            n = int(input())
        else:
            break

    N = input() # 덧셈할 숫자 입력

    nlist = list(N) # 입력한 숫자 한글자 단위로 리스트 초기화
    
    for i in range(0,n):
        result = result + int(nlist[i]) 

    print(result)