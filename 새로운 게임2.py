import sys
input = sys.stdin.readline

N, K = map(int,input().split())
#RLUD
dx = [0,0,-1,1]
dy = [1,-1,0,0]
'''
0 = white 이동하고자하는 방향이 흰색이면 이동하는대신에 A 와 A위에있는 모든말이 스택에 쌓인다
1 = red 일경우 이동하는 스택 reverse 시켜서 이동하는칸의 스택에 쌓는다
2 = blue 일경우 그칸으로 이동하지않고 dir 반대로 바꾼후 한칸을 이동해야하는데 이동해야하는칸이 맵밖이거나 파랑색일경우 stop
'''
board = [list(map(int,input().split())) for _ in range(N)]
stack = [[[] for _ in range(N)] for _ in range(N)]
for i in range(K):
    x, y, dir = map(int,input().split())
    stack[x-1][y-1].append([i,dir-1])
#해당스택에 있는 인덱스의 윗부분모두를 옮겨야함으로 해당인덱스번호가 나올떄까지 pop한다음 리버스 시킨리스트가 옮길 리스트이다.
def out(k, s):
    temp = []
    while True:
        i, dir = s.pop()      
        if i != k:
            temp.append([i,dir])
        elif i == k:      
            temp.append([i,dir])
            break
    temp.reverse()
    return temp
#만약 다음칸이 파랑색이거 나 맵밖이라면 방향을 바꿔준다.  
# for a,b in stack 으로 
# b = ?인 값을 대입하더라도 실제 스택의값은 안바뀌어서 애를 먹었다.      
def meetBlue(k,stack):
    #리스트내의 값을 바꾸려면 일일히 돌아가면서 바꿔야한다. for a,b in stack을 통하여 b를 바꾸더라도 리스트안의 b값은 안바뀐다 
    for i in range(len(stack)):
        if stack[i][0] == k:
            if stack[i][1] == 0:
                stack[i][1] = 1
            elif stack[i][1] == 1:
                stack[i][1] = 0                
            elif stack[i][1] == 2:
                stack[i][1] = 3
            elif stack[i][1] == 3:
                stack[i][1] = 2
#각 스택의길이를 측정하면서 4이상의 길이를 가지는게 있으면 True 반환
def check(stack):
    for i in range(N):
        for j in range(N):
            if len(stack[i][j])>=4:
                return True
    return False
#모든 스택을 돌면서 index값이 있는 x,y좌표와방향을 반환해주는함수
def find(idx):
    for i in range(N):
        for j in range(N):
            if stack[i][j]:
                for a,dir in stack[i][j]:
                    if a == idx:
                        return i,j,dir
time = 0  
while time<1001:
    #탈출조건.
    if check(stack):
        break
    #0~K까지 순서대로 움직인다.
    for i in range(K):
        #문제를 잘읽자ㅠㅠ 모든 움직임이끝난뒤의 길이가 4인줄알았더니 움직이는 도중에도 4이상의 길이가 생기면 탈출하여야한다
        if check(stack):
            break
        x,y,dir = find(i)
        #다음 좌표값.
        nx,ny = x+dx[dir], y+dy[dir]
        #다음칸이 블럭안이라면
        if 0<=nx<N and 0<=ny<N:
            #만약 이동하려는 칸의 색이 흰색이라면
            if board[nx][ny] == 0:
                #이동하려는 리스트를
                temp = out(i,stack[x][y])
                #그냥 이어주기
                stack[nx][ny].extend(temp)
            #만약 이동하려는 칸의 색이 빨간색이라면
            elif board[nx][ny] == 1:
                #이동하려는 리스트를
                temp = out(i,stack[x][y])
                #거꾸로 돌려서 이어주기
                stack[nx][ny].extend(reversed(temp))
            #만약 이동하려는 칸의 색이 파랑색이면
            elif board[nx][ny] == 2:
                #일단 해당인덱스 방향 바꿔준다.
                meetBlue(i,stack[x][y])
                #움직이고자했던방향의 반대칸 구하기
                bx, by = x - dx[dir], y - dy[dir]
                #만약 보드 안이라면
                if 0<=bx<N and 0<=by<N:
                    #흰색일때는 그냥붙이고
                    if board[bx][by] == 0:
                        temp = out(i,stack[x][y])
                        stack[bx][by].extend(temp)
                    #발강색일떄는 리버스시켜서 붙인다
                    elif board[bx][by] == 1:
                        temp = out(i,stack[x][y])
                        stack[bx][by].extend(reversed(temp))
                    #파랑색이거나 밖이면 아무일도 일어나지 않는다.
        #만약 이동하고자 하는칸이 보드 밖이면 파랑색과 같은일이 일어난다.
        else:
            meetBlue(i,stack[x][y])
            bx, by = x - dx[dir], y - dy[dir]
            if 0<=bx<N and 0<=by<N:
                if board[bx][by] == 0:
                    temp = out(i,stack[x][y])
                    stack[bx][by].extend(temp)
                elif board[bx][by] == 1:
                    temp = out(i,stack[x][y])
                    stack[bx][by].extend(reversed(temp))
    time+=1

print(time if time!=1001 else -1)
