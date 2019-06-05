# 문제출처: https://www.acmicpc.net/problem/10828

def enter_command_count():
    while 1:
        command_line = int(input())
        if command_line >= 0 and command_line <=10000:
                return command_line
        else:
                continue

if __name__ == "__main__":
    print(enter_command_count())