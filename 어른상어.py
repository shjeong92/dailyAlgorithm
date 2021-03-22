import sys

input = sys.stdin.readline
#N*N맵 M마리의 상어 k초유지되는 냄새
N, M, k = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
prior_direction = [[None]]
start_dir = list(map(int,input().split()))

for _ in range(M):
    temp =[]
    for _ in range(4):
        a,b,c,d = map(int,input().split())
        temp.append([a-1,b-1,c-1,d-1])
    prior_direction.append(temp)

#각번호의 상어의 p_dir = 각칸에 맞게끔 배치해놓았다.

shark_position=[]
for shark_num in range(1,M+1):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == shark_num:
                #상어번호, x좌표, y좌표, 상어 상어의 방향을 담아준다.
                shark_position.append([shark_num,i,j,start_dir[shark_num-1]-1])
                graph[i][j] = 0

#방향 UP, DOWN, LEFT, RIGHT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#상어가 있느 좌표에 냄새 생성하기.
def make_smell(graph,shark_position):
    
    for shark in shark_position:
        shark_num, i, j = shark[:-1]

        graph[i][j] = [shark_num, k]
#상어 이동후 냄새 -1 해주는 함수
def smell_minus(graph):
    for i in range(N):
        for j in range(N):
            #냄새인경우 길이가 2인 배열
            if graph[i][j]!=0:
                #냄새 감소후 0 이되면 빈칸으로 바꿔준다.
                if graph[i][j][1] > 0:
                    graph[i][j][1] -= 1
                if graph[i][j][1] == 0:
                    graph[i][j] = 0
#상어의 다음 방향을 정하는 함수
def set_shark_direction(shark_position,graph):
    updated_shark_position = []
    for shark in shark_position:
        shark_num, x, y, direction = shark
    
        #갈방향을 찾았는지 표시하기위함
        found = False
        for dir in prior_direction[shark_num][direction]:
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    updated_shark_position.append([shark_num, x, y, dir])
                    found = True
                    break

        #만약에다음 방향을 찾지 못하였다면 자신의 냄새가 있는 방향으로갑니다.
        if not found:
            for dir in prior_direction[shark_num][direction]:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < N and 0 <= ny < N and  graph[nx][ny] != 0:
                    if graph[nx][ny][0] == shark_num:
                                    
                        updated_shark_position.append([shark_num, x, y, dir])
                        found = True
                        break

    
    return updated_shark_position

def move_shark(shark_position):
    updated_shark_position = []
    for shark in shark_position:
        shark_num, x, y, dir = shark
        updated_shark_position.append([shark_num,x+dx[dir],y+dy[dir],dir])
    return updated_shark_position
#같은공간에 여러마리 상어가들어있을 경우 작은번호만 남고 나머지 상어는 내보내기 위한함수.
def kick_shark(shark_position):
    updated_shark = []
    #pop으로 하니 인덱스 가꼬여서 없애야하는 상어 [0] 으로 바꿔주고 마지막에 [0]이 아닌 값만 리스트에 삽입후 리턴함.
    for i in range(len(shark_position)-1,0,-1):
        for j in range(i-1,-1,-1):
            if shark_position[i][1:3] == shark_position[j][1:3]:
                shark_position[i] =[0]
    for shark in shark_position:
        if shark != [0]:
            updated_shark.append(shark)
    return updated_shark
time = 0

while True:
    #1000초를 초과하거나, 상어가 한마리 남는다면 반복문 종료
    if len(shark_position)==1 or time>1000:
        break
    make_smell(graph,shark_position)
    shark_position = set_shark_direction(shark_position,graph)
    shark_position = move_shark(shark_position)
    shark_position = kick_shark(shark_position)
    smell_minus(graph)
    time+=1
    
print(time if time<1001 else -1)
