import sys

if __name__ == "__main__":

    numberSubject  = int(sys.stdin.readline()) # 시험 과목 개수
    scoreList = list(map(int, sys.stdin.readline().split())) # 실제 시험 점수 리스트
    
    highestScore = max(scoreList) # 시험 최고 점수
    
    totalScore = 0 # 조작 점수 합계 선언 및 초기화

    for i in range(numberSubject):
        manipulatedScore = scoreList[i]/highestScore*100 # 시험 점수 조작하기
        totalScore = totalScore + manipulatedScore # 조작한 시험 점수 합계

    print(round(totalScore/numberSubject,2)) # 조작한 시험 점수 평균