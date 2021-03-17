from collections import deque
def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y = pos[0]
    pos2_x, pos2_y = pos[1]
    #상,하,좌,우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    #있는 그대로 이동하는경우
    for i in range(4):
        pos1_nx, pos1_ny, pos2_nx, pos2_ny = pos1_x + dx[i], pos1_y + dy[i] , pos2_x + dx[i], pos2_y + dy[i]
        if board[pos1_nx][pos1_ny] == 0 and board[pos2_nx][pos2_ny] == 0:
            next_pos.append({(pos1_nx, pos1_ny), (pos2_nx, pos2_ny)})
    
    #가로 = > 세로
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
                next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})

    #세로 => 가로
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)})
                next_pos.append({(pos2_x,pos2_y),(pos2_x,pos2_y+i)})
    return next_pos    
    
def solution(board):
    N = len(board)
    
    newBoard = [[1]*(N+2) for _ in range(N+2)]
    #벽생성
    #벽이 생성됨으로써 자연스럽게 1부터 시작하는 그래프로 바뀐다.
    for i in range(N):
        for j in range(N):
            newBoard[i+1][j+1] = board[i][j]
    #시작위치 set으로 - 블럭이 회전하면서 순서가 바뀌어도 같게하려고.
    pos = {(1,1), (1,2)}
    # set으로된 pos를 넣어줄것.
    visited = []
    q = deque()
    q.append((pos,0))
    
    while q:
        pos, time = q.popleft()
        #목적지 일경우 시간 리턴.
        if(N, N) in pos:
            return time
        
        for next_pos in get_next_pos(pos, newBoard):
            if next_pos not in visited:
                q.append((next_pos,time+1))
                visited.append(next_pos)
    
    return 0
