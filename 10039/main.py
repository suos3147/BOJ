# 문제출처: https://www.acmicpc.net/problem/10039
def enter_score():
    while 1:
        score = int(input())
        if score >= 0 and score <= 100:
            break
        else:
            continue
    return score

if __name__ == "__main__":
    total_score = 0

    for i in range(5):
        score = enter_score()
        if score < 40:
            score = 40
        total_score += score

    print(total_score//5)