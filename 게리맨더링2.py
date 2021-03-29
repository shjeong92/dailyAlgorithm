import sys
input = sys.stdin.readline
N = int(input())
data = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    data[i][1:] = list(map(int,input().split()))
#선택된 기준점에서 조건에  d1,d2리스트 만들기
def setD(x,y):
    temp = []
    result = []
    for i in range(1,N):
        for j in range(1,N):
            if 1<=x < x+i+j <= N:
                temp.append((i,j))
    for a,b in temp:
        if 1<=y-a < y < y+b <= N:
            result.append((a,b))
    return result
#구역을 나눠주는 함수
def boundary(x,y,d1,d2):
    temp = [[0]*(N+1) for _ in range(N+1)]
    #경계선 그려주기
    for i in range(d1+1):
        temp[x+i][y-i] = 5
    for i in range(d2+1):
        temp[x+i][y+i] = 5
    for i in range(d2+1):
        temp[x+d1+i][y-d1+i] = 5
    for i in range(d1+1):
        temp[x+d2+i][y+d2-i] = 5
    #한줄에 5가 두개 있다면 그 5와 5사이에있는 0은 5로 바꿔주기
    for i in range(1,N+1):
        if temp[i].count(5) == 2:
            flag = 0
            for j in range(1,N+1):
                if temp[i][j] == 5:
                    flag+=1
                if flag == 2:
                    break
                if flag>0:
                    temp[i][j] = 5 
    #문제에 제시된 조건에 맞춰 1,2,3,4채워주기
    for i in range(1,N+1):
        for j in range(1,N+1):
            if temp[i][j] != 5:
                if 1<= i < x+d1 and 1<= j <= y:
                    temp[i][j] = 1
                elif 1 <= i <= x+d2 and y < j <= N:
                    temp[i][j] = 2
                elif x+d1 <= i <= N and 1<=j<y-d1+d2:
                    temp[i][j] = 3
                elif x+d2 < i <= N and y-d1+d2<= j <= N:
                    temp[i][j] = 4
                else:
                    temp[i][j] = 5
    return temp

#나눠진 구역의 최대인원 - 최소인원 구하고 answer 갱신해주기
def mmcal(temp,data):
    global answer
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if temp[i][j] == 1:
                one += data[i][j]
            elif temp[i][j] == 2:
                two += data[i][j]
            elif temp[i][j] == 3:
                three += data[i][j]
            elif temp[i][j] == 4:
                four += data[i][j]
            elif temp[i][j] == 5:
                five += data[i][j]
    result = max(one,two,three,four,five) - min(one,two,three,four,five)
    if result < answer:
        answer = result
answer = 1e9
#맵 전체를 돌며 
for i in range(1,N+1):
    for j in range(1,N+1):
        dList = setD(i,j)
        #기준점에대한 d1,d2 가 존재한다면 
        if dList:
            #해당 기준점과 d1,d2에대한 값 계산하기
            for a, b in dList:
                temp = boundary(i,j,a,b)
                mmcal(temp,data)
print(answer)
