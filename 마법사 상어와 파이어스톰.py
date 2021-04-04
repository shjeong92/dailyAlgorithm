import sys
from collections import deque
input = sys.stdin.readline

#부분배열 시계방향으로 회전해주는 함수.
def rotate(arr,L):
    temp = [[0]*N for _ in range(N)]
    for k in range(0,N,L):
        for l in range(0,N,L):
            for i in range(k,k+L):
                for j in range(l,l+L):
                    temp[j-l+k][l+L-i+k-1] = arr[i][j]
    return temp
#얼음이 칸3개또는 인접해있지 않은 칸의 얼음양 -1 해주는 함수
def reduce(arr):
    temp = [[0]*N for _  in range(N)]

    for i in range(N):
        for j in range(N):
            cnt = 0

            for k in range(4):
                nx, ny = i+dx[k] ,j+dy[k]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] != 0:
                    cnt += 1
            
            if cnt <3 and arr[i][j] > 0:
                temp[i][j] = arr[i][j]-1
            else:
                temp[i][j] = arr[i][j]
    return temp
#연결된 구역의 넓이를 반환해주는함수
def bfs(x,y):
    q = deque([[x,y]])
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N  and not visited[nx][ny] and board[nx][ny] > 0:
                visited[nx][ny] = 1
                count += 1
                q.append([nx,ny])
    return count


N, Q = map(int,input().split())
N = 2**N
board = [list(map(int,input().split())) for _ in range(N)]
magic = list(map(int,input().split()))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
answer = 0
MAX = 0
#파이어스톰 & 감소
for i in range(len(magic)):
    L = 2**magic[i]
    board = rotate(board,L)
    board = reduce(board)
visited = [[0]*N for _ in range(N)]
#남아있는 모든얼음 더하기
for i in range(N):
    for j in range(N):
        answer += board[i][j]
#가장 큰 구역 구하기
for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j]!=0:
            visited[i][j] = 1
            MAX = max(bfs(i,j),MAX)
print(answer)
print(MAX)
