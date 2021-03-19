#생긴걸 보면 dp로 풀수있을거 같다. 만약에 움직일 수 있는방향이 오른쪽 아랫쪽이라면 dp로 풀수 있다 문제를 제대로 읽지않고 dp로 호다닥풀었다가 틀렸다.
#다익스트라를 이용한 풀이
import sys
import heapq
input = sys.stdin.readline
#입력받을 테스트케이스 갯수
T = int(input())
INF = int(1e9)
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(T):
    N = int(input())
    
    graph = [list(map(int,input().split())) for _ in range(N)]
    distance =[[INF]*N for _ in range(N)]
    #시작점
    x, y = 0, 0
    distance[x][y] = graph[x][y]
    #cost, x,y
    q=[(graph[x][y],x,y)]
    #다익스트라
    while q:
        dist, x, y = heapq.heappop(q)
        if dist < distance[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < N:
                cost = dist + graph[nx][ny]
                
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,nx,ny))
    #0,0 to N-1,N-1 최소거리.
    print(distance[N-1][N-1])
