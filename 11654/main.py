# 문제출처: https://www.acmicpc.net/problem/11654

if __name__ == "__main__":

    while 1:
        try:
            user_input = ord(input())
            if user_input >= 48 and user_input <= 57:
                break
            elif user_input >= 65 and user_input <= 90:
                break
            elif user_input >= 97 and user_input <=122:
               break

        except TypeError:
            continue
    
    print(user_input)