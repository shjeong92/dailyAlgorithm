import sys

input = sys.stdin.readline
#정답률이 25프로도 안되길래 어려운문젠가 싶었는데 그냥 수학문제였다.
N = int(input())
classes = list(map(int,input().rstrip().split()))

B, C = map(int,input().split())

cnt = 0
for i in classes:
    students = i
    if students - B<= 0:
        cnt += 1
        continue
    else:
        students -= B
        cnt += 1
        if students%C == 0:

            cnt+=students//C
            
        else:
            cnt+=students//C+1
print(cnt)
