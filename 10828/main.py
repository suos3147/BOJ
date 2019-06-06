# 문제출처: https://www.acmicpc.net/problem/10828

if __name__ == "__main__":
    stack = []
    
    while True:
        try:
            command_line = int(input())
            if command_line >= 1 and command_line <= 10000:
                break
        except ValueError:
            continue
    
    while command_line != 0:
        command = input().split()

        if command[0] == 'push':
            stack.append(command[1])

        elif command[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack)-1])
                del stack[len(stack)-1]

        elif command[0] == 'size':
            print(len(stack))

        elif command[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)

        elif command[0] == 'top':
            print(stack[len(stack)-1])

        else:
            continue

        command = []
        command_line = command_line-1