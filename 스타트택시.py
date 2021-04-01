import sys
from collections import deque
input = sys.stdin.readline
N, M, Fuel = map(int,input().split())
#탑승자좌표 : 도착좌표를 담을 사전
dic = {}
#ULDR
dx = [-1,0,1,0]
dy = [0,-1,0,1]
#길과 벽 정보
graph = [list(map(int,input().split())) for _ in range(N)] 
#택시의 좌표
tx, ty = map(int,input().split())
#좌표가 0부터시작하게하기위해 빼주기
tx-=1
ty-=1
for i  in range(M):
    #시작좌표, 도착좌표 사전에 넣어주기
    sx, sy, ex, ey = map(int,input().split())
    dic[(sx-1,sy-1)] = (ex-1,ey-1)
def pickup():
    global Fuel,tx,ty
    visited = [[0]*N for _  in range(N)]
    #큐에 택시의시작지점과 연료를 담는다.
    q = deque([[tx,ty,Fuel]])
    #현재 가진연료로 태우러 갈 수 있는 모든 승객의 좌표를 구한다.
    result = []
    visited[tx][ty] = 1
    while q:
        x, y, f = q.popleft()
        #연료가 0보다 작다면 반복문 탈출해주기
        if f < 0:
            break
        #만약에 해당좌표가 사전에 있다면 결과에 남은 해당좌표까지 이동후남은 연료량과, 좌표를 결과에 넣어준다.
        if (x, y) in dic:
            result.append([f,x,y])
        #이동할수있는 좌표구하기.
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            #맵안이면서, 방문한적이 없고, 벽이 아닌경우
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and not graph[nx][ny]:
                #방문처리해주고
                visited[nx][ny] = 1
                #연료량-1해서 큐에넣어준다
                q.append([nx,ny,f-1])
    #큐에 태우러 갈 사람이 있다면
    if result:
        #문제의 조건에 맞게 가장가까운게 우선이고, 그다음 작은행번호우선, 작은열번호 우선으로 정렬해준다.
        result = sorted(result, key = lambda x:(-x[0],x[1],x[2]))
        #제일 첫번재값으로 연료, 택시좌표의값을 갱신해주고
        Fuel,tx,ty = result[0]
        # 목적지의 좌표를 구한후
        next = dic[(tx,ty)]
        # 해당 탑승자정보 삭제해준다.
        del dic[(tx,ty)]
        return next
    else:
        return False
#목적지 좌표로 이동하는 함수
def goDest(next_x,next_y):
    global tx,ty,Fuel
    visited = [[0]*N for _ in range(N)]
    #탑승좌표, cost를 담아준다.
    q = deque([[tx,ty,0]])
    while q:
        x, y, cost = q.popleft()
        #만약에 비용이 현재가진 연료보다 많다면 실패이다.
        if cost > Fuel:
            return False
        #목표지점에 도착한다면
        if x == next_x and y == next_y:
            #가격만큼 연료 까고,
            Fuel-=cost
            #들었던 연료 두배만큼 채워준다.
            Fuel+=cost*2
            #택시 좌표를 갱신해준다
            tx,ty = x, y
            #제대로 갔으면 True반환
            return True
        #해당칸에서 갈 수 있는 칸 큐에 삽입하기
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and not graph[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx,ny,cost+1])
    #맵을 모두 탐색했는데 답이 안났다면 목적지로 못가는경우이다.
    return False
#사전에서 탑승자 정보가 모두 사라질때까지
while dic:
    next = pickup()
    if next == False:
        Fuel=-1
        break
    else:
        next_x, next_y = next
        if not goDest(next_x,next_y):
            Fuel=-1
            break
print(Fuel)
