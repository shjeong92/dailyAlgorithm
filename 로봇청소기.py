import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
x, y ,dir = map(int,input().split())
visited = [[0]*M for _ in range(N)]
board = [list(map(int,input().split())) for _ in range(N)]

def bfs(x,y,dir):
    count = 1
    #처음좌표 큐에담고 방문처리후 청소카운트1
    q = deque([(x,y,dir)])
    visited[x][y] = 1
    while q:
        x,y,dir = q.popleft()
        #청소할곳 찾는지 확인하는 플래그
        found = False
        #왼쪽으로 돌면서 청소할수있는곳이 있는지 찾는다
        for i in range(4):
            dir = (dir-1)%4
            nx,ny = x+dx[dir], y+dy[dir]
            #만약 찾으면 방문처리, 카운트올리고 큐에 해당좌표 추가후 포문탈출.
            if visited[nx][ny] == 0 and board[nx][ny] == 0:
                found = True
                visited[nx][ny] = 1
                count += 1
                q.append((nx,ny,dir))
                break
        #만약 뒤로 한칸이동후 다시 
        if not found:
            bx, by = x-dx[dir],y-dy[dir]
            if not(0<=bx<N and 0<=by<M) or board[bx][by] == 1:
                break
            else:
                q.append((bx,by,dir))

    return count

print(bfs(x,y,dir))
    
