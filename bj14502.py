import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx =[0,0,-1,1]
dy =[1,-1,0,0]
wallable = []
#벽 생성이 가능한 좌표 담기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            wallable.append([i, j])

#벽을3개 세울 수 있는 모든 경우의수구하기
candidates = list(combinations(wallable,3))

def bfs(x,y,c_graph,c_visited):
    q = deque([[x,y]])
    while q:

        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and c_graph[nx][ny] == 0:
                c_graph[nx][ny] = 2
                c_visited[nx][ny] = 1
                q.append([nx,ny])

answer = 0

for candidate in candidates:
    #deepcopy모듈 쓰는것보다 배열 만들어놓고 복사하는게 두배빨랐음.
    c_graph = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            c_graph[i][j] = graph[i][j]

    c_visited =[[0]*M for _ in range(N)]
    for x, y in candidate:
        c_graph[x][y] = 1
    #벽을 세운 그래프 순회중 바이러스라면 퍼질수있게 bfs
    for i in range(N):
        for j in range(M):
            if c_graph[i][j] == 2 and not c_visited[i][j]:
                bfs(i, j, c_graph, c_visited)
    
    cnt = 0
    #안전지대 0 의 갯수세기
    for i in range(N):
        for j in range(M):
            if c_graph[i][j] == 0:
                cnt += 1
    #가장큰값으로 초기화하기
    answer = max(answer, cnt)
print(answer)
