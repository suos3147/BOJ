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

class Stack:
    def setdata(self, count, command, stack):
        self.count = count
        self.command = command
        self.stack = stack

    def push(self):
        if self.command.find(" ",5) != -1:
            command, num = self.command.split()
            self.stack.append(num)
    

if __name__ == "__main__":
    s = Stack
    s.setdata(enter_count, enter_command)
    