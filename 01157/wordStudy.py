# 문제출처: https://www.acmicpc.net/problem/1157
def enter_string():
    try:
        str = input().upper()
    except ValueError:
        return enter_string
    if len(str) <= 1000000:
        return str
    else:
        return enter_string

def print_alphabet(str):
    str = list(str)
    count_list = {}
    for i in range(len(str)):
        for j in range(len(str)):


if __name__ == "__main__":
    enter_string()