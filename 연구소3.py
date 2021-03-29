import sys,copy
from itertools import combinations as combi
from collections import deque
input = sys.stdin.readline

#M개뽑힌 바이러스좌표담긴q, 연구소, 빈칸의갯수
def bfs(q,graph,empty_cnt):
    global answer
    graph = copy.deepcopy(graph)
    visited = [[0]*N for _ in range(N)]
    #바이러스 좌표 방문처리
    for a, b in q:
        visited[a][b] = 1
    result = 0
    #q 에 값이있을동안돌기
    while q:
        #만약에 비활성 바이러스를 방문하지 않았을때도 모든 빈칸이 바이러스로 뒤덥혔을때 종료해주기
        if not empty_cnt:
            break
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                empty_cnt-=1
                graph[nx][ny] = 2
                q.append((nx,ny))
            #비활성화 바이러스를 방문했을때도 큐에 넣어줘야한다 하지만 빈칸횟수는 줄어들지않음.
            elif 0<=nx<N and 0<=ny<N and graph[nx][ny] == 2 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))

    for i in range(N):
        for j in range(N):
            #만약에 빈칸이 하나라도 발견된다면 탈출
            if graph[i][j] == 0:
                return
    #모든 빈칸이 감염된경우 visited 의 최댓값이 총걸린시간
    #answer 최솟값 갱신해주기
    for i in range(N):
        for j in range(N):
            if visited[i][j] > result:
                result = visited[i][j]
    answer = min(answer,result-1)
    return

virus_pos = []
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus_pos.append((i,j))
        elif graph[i][j] == 0:
            cnt += 1
dx = [0,0,-1,1]
dy = [1,-1,0,0]
answer = int(1e9)
#모든 조합에대해서 bfs 돌리기
for candi in list(combi(virus_pos,M)):
    q = deque(candi)
    bfs(q,graph,cnt)

print(answer if answer != int(1e9) else -1)



