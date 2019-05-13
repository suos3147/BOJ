# 문제출처: https://www.acmicpc.net/problem/2920

if __name__ == "__main__":
    scale_list = input().split()
   
    if scale_list == [1, 2, 3, 4, 5, 6, 7, 8]:
        print("ascending")
    elif scale_list == [8, 7, 6, 5, 4, 3, 2, 1]:
        print("descending")
    else:
        print("mixed")