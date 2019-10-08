"""
로봇이 움직일 횟수 N
왼쪽으로 방향을 바꿀 확률 L/(L+M+R)
가만히 있을 확률 M/(L+M+R)
오른쪽으로 방향을 바꿀 확률 R/(L+M+R)
"""
N, L, M, R = map(int, input().split())
result = 0  # 로봇이 원점으로 부터 떨어져 있는 정도 x^2 + y^2

l = L/(L+M+R)
m = M/(L+M+R)
r = R/(L+M+R)

for i in range(N):
