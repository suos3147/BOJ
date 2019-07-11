import sys

if __name__ == "__main__":
    c = int(sys.stdin.readline())
    for i in range(c):
        input_list = list(map(int,sys.stdin.readline().split()))

        average_score = sum(input_list[1:])/input_list[0]
        average_score_count = 0

        for j in input_list[1:]:
                if(average_score < j):
                        average_score_count += 1

        percetage = round(average_score_count/input_list[0]*100,3)

        print(str('%.3f' % percetage)+"%")
        