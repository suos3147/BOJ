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

if __name__ == "__main__":
    enter_string()