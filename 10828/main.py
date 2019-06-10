# 문제출처: https://www.acmicpc.net/problem/10828

def enter_count():
    try:
        count = int(input())
    except ValueError:
        return enter_count()

    if count >= 1 and count <=10000:
        return count
    else:
        return enter_count()

def enter_command():
    try:
        command = input()
        return command
    except ValueError:
        return enter_command()


def push(stack, input_command):
    try:
        command, num = input_command.split()
        if command == 'push':
            stack.append(num)
        else:
            return -1
    except ValueError:
        return -1

def pop(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.remove(stack[-1])

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
    
if __name__ == "__main__":
    s = []
    cnt = enter_count()

    while cnt != 0:
        cmd = enter_command()

        if cmd == 'pop':
            pop(s)
        elif cmd == 'size':
            size(s)
        elif cmd == 'empty':
            empty(s)
        elif cmd == 'top':
            top(s)
        else:
            if push(s, cmd) == -1:
                continue

        cnt -= 1