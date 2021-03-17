#python3에서는 시간초과납니다 ㅠㅠ.. pypy3에서는 통과하는 추후에 다시 .
import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int,input().split())

graph = [list(map(int,input().split())) for _  in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(graph,x,y,visited):
        
    q = deque([[x,y]])
    #x,y를 기준으로 연합 가능한지역을 담을 배열.
    union = [[x,y]]
    cnt = 1
    #x,y를 기준으로 연합 가능한지역의 값들을 합한후 cnt 로나눈값을 담을꺼.
    val = graph[x][y]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 이동할곳이 맵 안이어야함.
            if 0 <= nx < N and 0 <= ny < N:
                dif = abs(graph[x][y] - graph[nx][ny])
                #위 아래 왼 오른 중 한군데라도 연합이 가능하면 가능한것.
                if L <= dif <= R and dif != 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    union.append([nx,ny])
                    val += graph[nx][ny]
                    cnt += 1
    if cnt == 1:
        return False
    else:
        for x, y in union:
            graph[x][y] = int(val/(cnt))
        return True
answer = 0
while True:
    changed = False
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                k=bfs(graph,i,j,visited)
                if k:
                    changed = True
    #한바퀴 돌아도 연합을 만들수 없을경우 종료
    if not changed:
        break
    else:
        answer += 1
print(answer)
