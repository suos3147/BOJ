if __name__ == "__main__":
    userInput = input() #알파벳 소문자와 대문자로 이루어진 단어 입력
    
    """
    입력한 문자열 길이가 100이 넘거나 0이면 재입력
    """
    while 1:
        if len(userInput) > 100 or len(userInput)  == 0:
            userInput = input()
        else:
            break
    
    for listIndex in range(0,len(userInput),10):
        print(userInput[listIndex:listIndex+10])