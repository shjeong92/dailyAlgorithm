import sys
import copy
from collections import deque
input = sys.stdin.readline
N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
#상어의 첫크기
size = 2
#상어가 먹은물고기수 초기화용
eat = 0
shark =[]

for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == 9:
            shark =[i,j,size,eat]
            #상어 위치를 저장해주고 상어를 그래프에서 뺴준다 만약에 안뺄경우 상어가 물고기를 먹다가 사이즈가 9보다 커져서 그걸 먹었다고 할 수도 있기때문에
            graph[i][j] = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]
#fish [dist,x,y,size]
#상어가 먹을수 있는 물고기의 위치를 반환해주는 함수.
def radar(shark, g):
    fish = deque()
    #현재의 그래프를 복사
    graph = copy.deepcopy(g)
    visited = [[0]*N for _ in range(N)]
    x, y ,size= shark[0],shark[1],shark[2]
    dist = 0
    q = deque([[dist,x,y]])
    visited[x][y] = 1
    #BFS로 상어가 먹을수 있는 물고기 모두찾기.
    while q:
        dist, x, y= q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if graph[nx][ny] == 0 or graph[nx][ny] == size:
                    visited[nx][ny] = 1
                    q.append([dist+1,nx,ny])
                #먹을 수 있는 물고기 리스트 담을꺼!
                elif graph[nx][ny] < size:
                    visited[nx][ny] = 1
                    q.append([dist+1,nx,ny])
                    #물고기 거리, x좌표, y좌표
                    fish.append([dist+1,nx,ny])
    #먹을수 있는 물고기를 거리순으로 정렬한다// 만약 거리가 같은물고기가있으면 가장위쪽에있는물고기, 그래도 중복되면 가장 왼쪽에있는 물고기순으로 정렬해준다

    fish = sorted(fish,key = lambda x :(x[0],x[1],x[2]))
    return fish


#게임이 끝나는경우 = 레이더에 아무것도 안잡히는경우 
#shark =[x,y,size,eat]
time = 0
while True:
    fishList = radar(shark,graph)
    
    if fishList == []:
        break
    else:
        dist, x, y = fishList[0]
        time += dist
        shark[0],shark[1] = x, y
        shark[3] += 1
        graph[x][y] = 0
        #물고기먹고 진화하는경우
        if shark[3] == shark[2]:
            shark[2] += 1
            shark[3] = 0
    #여기 주석 해재하면 상어가 물고기 먹는 순서를 볼수 있어요
    # print("sharksize = ",shark)
    # for i in range(N):
    #     print(graph[i])
    # print("=========================")
print(time)
