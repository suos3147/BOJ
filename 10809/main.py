# 문제출처: https://www.acmicpc.net/problem/10809
import sys

if __name__ == "__main__":
    user_input = list(input())

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(len(user_input)):
        for j in range 26:
            if user_input[i] == alphabet[j]:
                alphabet[j] = user_input.index()
            else:
                alphabet[j] = -1             