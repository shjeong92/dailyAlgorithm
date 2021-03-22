import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

graph =[list(input().rstrip()) for _  in range(N)]

# R L U D
q = deque()
visited = {}
dx = [0,0,-1,1]
dy = [1,-1,0,0]



def move(x,y,dx,dy):
    count = 0
    #다음칸이 벽이거나, 현재칸이 구멍일 때까지.
    while graph[x+dx][y+dy] !='#' and graph[x][y] != 'O':
        x+=dx
        y+=dy
        count+=1
    #만약에 구슬이 똑같은위치로 이동했을때 더 멀리서부터온 구슬을 한칸 뒤로 물리기위해 count를 셈
    return x,y,count
#초기화
def init():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j
    #큐에 처음 구슬위치와 depth넣어주고 방문처리(딕셔너리 이용)
    q.append((rx,ry,bx,by,1))
    visited[(rx,ry,bx,by)] = True
def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        #열번넘어도 안되면 종료
        if depth > 10 :
            break

        for i in range(4):
            nrx,nry,r_count = move(rx, ry, dx[i],dy[i])
            nbx,nby,b_count = move(bx, by, dx[i],dy[i])
            #파랑구슬이 빠졌을경우 넘어가기.
            if graph[nbx][nby] == 'O':
                continue
            #빨강구슬이 빠졌을경우 성공
            if graph[nrx][nry] == 'O':
                print(depth)
                return
            #같은위치에 들어갔을경우 멀리서 온구슬을 한칸뒤로 이동시키기.
            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
                
            
            if (nrx,nry,nbx,nby) not in visited:
                visited[(nrx,nry,nbx,nby)] = True
                q.append((nrx,nry,nbx,nby,depth+1))
    print(-1)
bfs()
