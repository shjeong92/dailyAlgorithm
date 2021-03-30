import sys
from collections import defaultdict, deque
from itertools import chain
input = sys.stdin.readline


#원판 회전함수
def line_rotate(deque,dir,time):
    #시계방향
    if dir == 0:
        for _ in range(time):
            tmp = deque.pop()
            deque.insert(0,tmp)
    #시계반대방향
    elif dir == 1:
        for _ in range(time):
            tmp = deque.pop(0)
            deque.append(tmp)
#인접 삭제에 필요한 방향 RLUD
dx = [0,0,-1,1]
dy = [1,-1,0,0]
#인접한수가 같으면 0 으로 삭제해버리기
def bfs(q,visited):
    while q:
        x, y = q.popleft()
        found = False
        for i in range(4):
            nx, ny = x+dx[i], (y+dy[i])%M # 원이므로 첫값 끝값같은것도 생각해주기
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if circles[nx][ny] == circles[x][y] and circles[x][y] != 0:
                    found = True
                    visited[nx][ny] = 1
                    q.append((nx,ny))
        #같은값이 찾아졌을때 시작지점도 방문처리해주기
        if found:
            visited[x][y] = 1
#인접한 값(visited = 1) 인부분 0으로 만들어주기
def makeZero():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                circles[i][j] = 0
#만약에 인접동일값이 하나도 없다면 조건에 맞게 계산해주기
def calAvg():
    total = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                total+=circles[i][j]
                cnt+=1
    #ZeroDivisionError 방지하기위한 조건
    if cnt!=0:
        avg = total / cnt
        for i in range(N):
            for j in range(M):
                if circles[i][j] != 0:
                    if circles[i][j] > avg:
                        circles[i][j] -= 1
                    elif circles[i][j] < avg:
                        circles[i][j] += 1
#T 갯수만큼 값 받고 돌리고 계산하고~
N, M, T = map(int,input().split())
circles = [list(map(int,input().split())) for _ in range(N)]

for _ in range(T): 
    x, d, k = map(int,input().split())
    for i in range(N):
        if (i+1)%x == 0:
            #조건에맞는 원판 회전하기
            line_rotate(circles[i],d,k)
    visited = [[0]*M for _ in range(N)]
    #모든좌표값 q에넣고
    q = deque()
    for i in range(N):
        for j in range(M):
            q.append([i,j])
    #bfs돌리기
    bfs(q,visited)
    #지울 값이 있다면
    if sum(chain(*visited)):
        makeZero()
    #지울 값이 없다면
    elif sum(chain(*visited)) == 0:
        calAvg()
print(sum(chain(*circles)))
