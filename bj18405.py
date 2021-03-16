import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
virus = []
#S초 후의 X,Y 에 존재하는 바이러스의 종류 없다면 0출력해야함
S, X, Y = map(int,input().split())

#1보다 크거나 같으면 바이러스 [바이러스종류, 시간, x, y]
for i in range(N):
    for j in range(N):
        v = graph[i][j]
        if v >= 1:
            virus.append([v,0,i,j])
#낮은숫자의 바이러스 우선
virus = deque(sorted(virus))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
while virus:
    v, s, x, y = virus.popleft()
    if s == S:
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
            graph[nx][ny] = v
            virus.append([v,s+1,nx,ny])
print(graph[X-1][Y-1])