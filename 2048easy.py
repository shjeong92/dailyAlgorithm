import sys,copy
from itertools import chain
input = sys.stdin.readline
N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]
#0이 아닌 값들을 리스트에담아서 계산하는방식으로 풀었습니다.
#방향이 U,D 일경우 90% 왼쪽 회전후 계산한다음 다시 오른쪽으로 돌려놓는 방식입니다.
def rotate(board,direction):
    rotated = [[0]*N for _ in range(N)]
    if direction == 'R':
        for i in range(N):
            for j in range(N):
                rotated[i][j] = board[N-j-1][i]
    elif direction == 'L':
        for i in range(N):
            for j in range(N):
                rotated[i][j] = board[j][N-i-1]
    return rotated

def move(dir,board):
    board = copy.deepcopy(board)
    result = []
    if dir =='L' or dir == 'R':
        for i in range(N):
            temp =[]
            # 한줄 한줄 읽으며 0 이아닌값을 temp에 담고,
            for j in range(N):
                if board[i][j] != 0:
                    temp.append(board[i][j])
            #그렇게해서 만들어진 temp 를 merge 함수를통해 만들어진 결과값을 result에 넣어줍니다.
            result.append(merge(temp,dir))
    elif dir == 'U' or dir =='D':
        #U는 판을 왼쪽으로 90도 돌린후 L계산한것을 다시 오른쪽으로 돌린값과 같습니다
        #D는 판을 왼쪽으로 90도 돌린후 R계산한것을 다시 오른쪽으로 돌린값과 같습니다
        board = rotate(board,'L')
        for i in range(N):
            temp =[]
            for j in range(N):
                if board[i][j] != 0:
                    temp.append(board[i][j])
            if dir =='U':
                result.append(merge(temp,'L'))
            elif dir == 'D':
                result.append(merge(temp,'R'))
        result = rotate(result,'R')
    return result

def merge(temp,dir):
    made = []
    if dir =='L':
        #temp의 길이-1 까지 돌면서 뒷값과 비교
        for i in range(len(temp)-1):
            #같다면 앞값을 2로바꾸고 뒷값을 0으로 바꿉니다.
            if temp[i] == temp[i+1]:
                temp[i]*=2
                temp[i+1] = 0
            
            #0이아니라면 made에 넣어줍니다.
            if temp[i] != 0:
                made.append(temp[i])
        #마지막값은 포문안에서 해결안됐으므로, 만약 0이아니라면 made에 넣어줍니다.
        if temp and temp[-1] != 0:
            made.append(temp[-1])
        #판의 크기만큼 0을 오른쪽에 붙여줍니다.
        while len(made) != N:
            made.append(0)
    elif dir =='R':
        #방법은 같지만 왼쪽을 채워넣어야하기에 insert를 사용하였고
        for i in range(len(temp)-1,0,-1):
            if temp[i] == temp[i-1]:
                temp[i] *= 2 
                temp[i-1] = 0
            if temp[i]!= 0:
                made.insert(0,temp[i])
        if temp and temp[0] != 0:
            made.insert(0,temp[0])

        #0 또한 왼쪽에 채워야하기에 insert.
        while len(made) != N:
            made.insert(0,0)
    
    return made
answer = 0

def dfs(board,depth):
    global answer
    #5번 돌았을때 가장큰값을 업데이트후 종료합니다.
    if depth == 5:
        answer = max(max(list(chain(*board))), answer)
        return
    #실제 보드에 영향받지않게 복사합니다
    copied_board = copy.deepcopy(board)
    dfs(move('R',copied_board), depth+1)
    dfs(move('L',copied_board), depth+1)
    dfs(move('U',copied_board), depth+1)
    dfs(move('D',copied_board), depth+1)


dfs(board,0)
print(answer)
