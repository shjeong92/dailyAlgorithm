import sys
input = sys.stdin.readline
def rotate(sand):
    temp = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[5-j-1][i] = sand[i][j]
    return temp
move = []
# 중앙부터 달팽이 좌표와 방향 
def getPos():
    x = y = N//2
    dir = 0

    step = 1
    
    while True:
        if not(0<=x<N and 0<=y<N):
            break
        for _ in range(2):
            for _ in range(step):
                
                x+=dx[dir]
                y+=dy[dir]
                if not(0<=x<N and 0<=y<N):
                    break
                move.append([x,y,dir])
            dir = (dir+1)%4
        step+=1
    
N = int(input())
dx = [0,1,0,-1]
dy = [-1,0,1,0]
data =[list(map(int,input().split())) for _ in range(N)]
sand =[
    [0,0,2,0,0],
    [0,10,7,1,0],
    [5,-1,0,0,0],
    [0,10,7,1,0],
    [0,0,2,0,0]
]
#각방향별 토네이후 모래량% 좌표 담긴 리스트
cal_dir = []
getPos()      
for k in range(4):
    temp = []
    for i in range(5):
        for j in range(5):
            if sand[i][j]>0:
                #각방향별 중앙에서 남은모래좌표까지의 거리차이를 구하는것과 같음.
                temp.append([i-2,j-2,sand[i][j]])
    cal_dir.append(temp)
    sand = rotate(sand)

index = 0
answer = 0
for x,y,dir in move:
    tmp = 0
    for sx,sy,per in cal_dir[dir]:        
        nx, ny = x+sx, y+sy
        if 0<=nx<N and 0<=ny<N:
            data[nx][ny] +=  data[x][y]*per//100
        else:
            answer += data[x][y]*per//100
        tmp += data[x][y]*per//100
    if 0<= x + dx[dir] < N and 0<= y + dy[dir] <N:
        data[x+dx[dir]][y+dy[dir]] += data[x][y] - tmp
    else:
        answer += data[x][y] - tmp
    data[x][y] = 0
    
print(answer)
