import sys
from collections import deque
input = sys.stdin.readline

R, C, T = map(int,input().split())

room  = [list(map(int,input().split())) for _ in range(R)]
up = 0
down = 0

for i in range(R):
    if room[i][0] == -1:
        up = i
        down = i+1
        break

def spread(room):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    q = deque()
    for i in range(R):
        for j in range(C):
            if room[i][j] not in [-1,0]:
                q.append([room[i][j],i,j])
    
    while q:
        v,x,y = q.popleft()
        cnt = 0
        value = v//5
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx <R and 0<= ny <C and room[nx][ny] != -1:
                cnt += 1
                room[nx][ny] += value
        
        room[x][y] -= value*cnt
def move_up():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    dir = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        #공기청정기 도착시 반복문탈출
        if x == up and y ==0:
            break
        #끝점에 도달했을때 방향바꿔주기.
        if nx<0 or nx>=R or ny <0 or ny >=C:
            dir += 1
            continue
        #한칸씩 푸시푸시
        room[x][y] , before = before, room[x][y]
        x, y = nx, ny
def move_down():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dir = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        #공기청정기 도착시 반복문탈출
        if x == down and y == 0:
            break
        #끝점에 도달했을때 방향바꿔주기.
        if nx<0 or nx>=R or ny <0 or ny >=C:
            dir += 1
            continue
        #한칸씩 푸시푸시
        room[x][y] , before = before, room[x][y]
        x, y = nx, ny
#T초동안 반복
for _ in range(T):
    spread(room)
    move_up()
    move_down()
answer = 0
#0보다크면 먼지임
#정답에 더해주기
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            answer += room[i][j]
print(answer)
