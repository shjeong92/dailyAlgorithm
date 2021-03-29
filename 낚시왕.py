import sys
input = sys.stdin.readline
#상어가 움직힌후의 좌표와 방향을 계산해주는 함수
#상어최대마릿수*최대초 = 10000*1000 초단위로 움직이게 하여도 충분할거라 생각했지만 python3에서 시간초과가 났다 pypy3는 무사히통과
#상어이동좌표계산을 효율적으로하면 python3도 통과할것 같다.
def cal_pos(x,y,speed,dir):
    nx,ny = x,y
    if dir == 1:
        for _ in range(speed):
            if nx == 1 and dir == 1:
                dir = 2
            elif nx == N and dir == 2:
                dir = 1
            nx += dx[dir]
    elif dir == 2:
        for _ in range(speed):
            if nx == 1 and dir == 1:
                dir = 2
            elif nx == N and dir == 2:
                dir = 1
            nx += dx[dir]
    elif dir == 3:
        for _ in range(speed):
            if ny == 1 and dir ==4:
                dir = 3
            elif ny == M and dir ==3:
                dir = 4
            ny += dy[dir]
    elif dir == 4:
        for _ in range(speed):
            if ny == 1 and dir ==4:
                dir = 3
            elif ny == M and dir ==3:
                dir = 4
            ny += dy[dir]
    return nx, ny, dir
def move(board):
    new_board = [[[0,0,0]]*(M+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,M+1):
            if board[i][j] != [0,0,0]:
                size, speed, dir = board[i][j]
                nx,ny,dir = cal_pos(i,j,speed,dir)
                #현재 보드에서 움직임을 진행해 버리면 아직 움직이지 않은 상어를 잡아 먹으므로 새로운 보드에서 이동한다.
                if new_board[nx][ny][0] < size:
                    new_board[nx][ny] = [size,speed,dir]
    return new_board

N, M, S = map(int,input().split())
board = [[[0,0,0]]*(M+1) for _ in range(N+1)]
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
for _ in range(S):
    #좌표//속력 방향 크기
    x, y, s, d, z = map(int,input().split())
    board[x][y] = [z,s,d]
#사람의 시작좌표
human = 0
answer = 0
while True:
    #사람한칸오른쪽으로 이동하고
    human+=1
    #만약 맵밖이면 종료
    if human > M:
        break
    #가장 가까운 상어 한마리 잡고 반복문 탈출
    for i in range(1,N+1):
        if board[i][human] != [0,0,0]:
            answer += board[i][human][0]
            board[i][human] = [0,0,0]
            break
    board = move(board)
print(answer)
