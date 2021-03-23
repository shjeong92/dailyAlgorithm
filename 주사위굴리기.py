import sys
input = sys.stdin.readline
N, M, x, y, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
order = list(map(int,input().split()))
#위 북 동 서 남 아래
dice = [0 for _ in range(6)]
#동서북남
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]


for dir in order:
    nx = x + dx[dir]
    ny = y + dy[dir]
    #굴린 값이 보드 안이어야함
    if 0 <= nx < N and 0 <= ny < M:
        
        #동,서 방향으로 회전시 주사위의 북,남 방향은 변하지 않고 나머지 방향은 스왑시켜줌
        if dir == 1:
            dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
        elif dir == 2:
            dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]


        #북, 남 방향으로 회전시 주사위의 동,서 방향은 변하지 않고 나머지 방향은 스왑
        elif dir == 3:
            dice[0],dice[1],dice[4],dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        #현재 보드값이 0 이라면 주사위의 바닥값이 보드에 입혀짐
        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]
        #현재 보드값이 0이 아니라면 주사위의 바닥값은 보드의 값이되고 보드는 0으로 바꿔줌.
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        #주사위 윗부분 출력
        print(dice[0])
