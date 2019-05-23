# 문제출처: https://www.acmicpc.net/problem/10809
import sys

if __name__ == "__main__":
    print_list = [0]*26
    user_input = list(input())

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(len(alphabet)):
        for j in range(len(user_input)):
            if user_input[j] == alphabet[i]:
                print_list[i] = user_input.index(alphabet[i])
                break
            else:
                print_list[i] = -1
        
    for i in range(len(print_list)):
        sys.stdout.write(str(print_list[i])+" ")
    