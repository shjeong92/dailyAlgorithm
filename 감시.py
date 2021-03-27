import sys, copy
input = sys.stdin.readline

def dfs(start,board,cctv):
   global MIN
   #모든 cctv를 확인한경우 MIN값 갱신해주기
   if start == len(cctv):
      cnt = 0
      for i in range(N):
         for j in range(M):
            if board[i][j] == 0:
               cnt += 1
      MIN = min(MIN, cnt)
      return
   num, x, y = cctv[start]

   for dir in dc[num]:
      #실제보드에 영향가지않게 복사해주기
      tmp = copy.deepcopy(board)
      #각 카메라가 감시할 수 있는 모든방향으로 탐색하기.
      for i in dir:
         nx, ny = x + dx[i], y + dy[i]
         while 0 <= nx < N and 0 <= ny < M:
            if tmp[nx][ny] == 6:
               break
            elif tmp[nx][ny] == 0:
               tmp[nx][ny] = '#'
            
            nx += dx[i]
            ny += dy[i]
      dfs(start+1,tmp,cctv)
   
MIN = int(1e9)
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
#R L U D
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
#감시 카메라의 방향
dc = [
   [],
   [[0],[1],[2],[3]],
   [[0,1],[2,3]],
   [[2,0],[2,1],[3,0],[3,1]],
   [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
   [[0,1,2,3]]
]
cctv = []
for i in range(N):
   for j in range(M):
      if board[i][j] not in [0,6]:
         #cctv번호, x, y 좌표 저장하기
         cctv.append((board[i][j],i,j))
dfs(0,board,cctv)
print(MIN)
