# 문제출처: https://www.acmicpc.net/problem/8958

if __name__ == "__main__":
    testcase = []
    test_count = int(input())
    
    for i in range(test_count):
        score = 0
        total_score = 0
        testcase.append(list(input()))
        for j in range(len(testcase[i])):
            if testcase[i][j] == 'O':
                score += 1
                total_score += score
            else:
                score = 0
        print(total_score)