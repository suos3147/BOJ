# 문제출처: https://www.acmicpc.net/problem/10809
import sys

if __name__ == "__main__":
    user_input = list(input())

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if user_input[0] == alphabet[0]:
        alphabet[0] = user_input.index(alphabet[0])
    else:
        alphabet[0] = -1

    print(alphabet)
    