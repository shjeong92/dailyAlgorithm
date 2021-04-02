import sys
from collections import deque
input = sys.stdin.readline
#맵에있는 파이어볼 이동시키는 함수
def moveFireBall(graph):
    temp_graph = [[[] for _ in range(N)] for _ in range(N)]
    #파이어볼 이동시키기
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                #보드에 들어있는 파이어볼 꺼내서
                while graph[i][j]:
                    w, s, d = graph[i][j].pop()
                    #속도만큼 이동해주기 보드의끝과 첫번째는 연결돼있으므로 %N 해줌
                    nx, ny = (i+dx[d]*s)%N, (j+dy[d]*s)%N
                    temp_graph[nx][ny].append([w,s,d])
    #이동시킨 그래프 반환
    return temp_graph
 #파이어볼 합치고 
def combAndDiv(graph):
    temp_graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            #만약 한칸에 여러개의 파이어볼있을경우 무개의 합과 스피드의 합을 구하기위한 변수
            tw = ts = 0
            #모두 똑같은방향이었는가 아니었는가 판단하기위한 변수
            td = ''
            #길이가 1보다 클경우
            if len(graph[i][j])>1:
                #추후에 속도나누기위한
                size = len(graph[i][j])
                #방향확인용 플래그
                dif = False
                while graph[i][j]:
                    w, s, d = graph[i][j].pop()
                    tw += w
                    ts += s
                    #방향플레그 비어있을경우 첫값을 넣어주고,
                    if td == '':
                        td = d%2
                    #그다음방향부터 첫방향%2값과 일치하지않으면 모두 홀수이거나 짝수가 아닌경우이다.
                    else:
                        if td != d%2:
                            dif = True
                #문제에서 제시해준 방향
                if dif == True:
                    dir = [1,3,5,7]
                else:
                    dir = [0,2,4,6]
                #만약 무게가 0이면 무시해도 좋다.
                if tw//5>0:
                    #무게가 1이상이라면 네개로 나누어진 파이어볼 리스트에넣기
                    for k in range(4):
                        temp_graph[i][j].append([tw//5,ts//size,dir[k]])
            #삼성 문제는 항상 설명이 2% 부족한것같다.
            #이것때문에 시간 많이날림 길이가 한개일경우 나누어지지 않고 그냥 이동만한다.
            #
            elif len(graph[i][j]) == 1:
                temp_graph[i][j] = graph[i][j]
    return temp_graph


N, M, K = map(int,input().split())
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
graph = [[[] for _ in range(N)] for _ in range(N)]
#초기 값 넣어주기
for _ in range(M):
    x, y, weight, speed, dir = map(int,input().split())
    graph[x-1][y-1].append([weight,speed,dir])
while K>0:
    K -= 1
    #이동시킨 파이어볼 본래그래프에 옮기고                    
    graph = moveFireBall(graph)
    #파이어볼 합치고 나누고
    graph = combAndDiv(graph)
answer = 0
#모든칸을 확인하며 파이어볼이있을경우
#모든무게를 정답에 더하기
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            for a,b,c in graph[i][j]:
                answer += a
print(answer)
