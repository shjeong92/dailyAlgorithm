import sys
from itertools import chain
from typing import Counter
input = sys.stdin.readline
#아래로가는보드 오른쪽으로 돌려서 편하게 계산하고 다시 원래대로 돌려놓기위함
def rotate(board,dir):
    h = len(board)
    w = len(board[0])
    temp = [[0]*h for _ in range(w)]
    #왼쪽회전
    if dir == 0:
        for i in range(h):
            for j in range(w):
                temp[w-j-1][i] = board[i][j]
    #오른쪽회전
    elif dir == 1:
        for i in range(h):
            for j in range(w):
                temp[j][h-i-1] = board[i][j]
    return temp
#각각의 보드에 타일을 넣어주는함수
def putTile(type,x,y):
    if type == 1:
        board_r[x][y] = 1
        board_d[x][y] = 1
    elif type == 2:
        board_r[x][y] = 1
        board_r[x][y+1] = 1
        board_d[x][y] = 1
        board_d[x][y+1] = 1
    elif type == 3:
        board_r[x][y] = 1
        board_r[x+1][y] = 1
        board_d[x][y] = 1
        board_d[x+1][y] = 1
#타일을 놓은다음 움직일 수 있는 만큼 이동시켜주는 함수
def tileMove(board):
    jump = 1e9
    block = []
    #이동할수 있는 최댓값중 작은값을 채택하여
    for i in range(4):
        for j in range(4):
            if board[i][j] == 1:
                board[i][j] = 0
                block.append([i,j])

                #0 0 0 0 0 0
                cnt = 0
                for k in range(j+1,10):
                    if board[i][k] == 0:
                        cnt += 1
                    else:
                        break
                #만약 0 이라면 세지않는다 블럭모양이 1 1 일경우 왼쪽 1 은 무시해줘도됨
                if cnt !=0:
                    jump = min (jump,cnt)
    #타일 이동
    for x, y in block:
        board[x][y+jump] = 1
#6~9번줄에서 라인이 타일로 꽉차있다면 해당라인 pop 후 첫줄 끼워주기
def checkLine(board):
    global answer
    for j in range(6,10):
        isLine = True
        for i in range(4):
            if board[i][j] == 0:
                isLine = False
        if isLine:
            answer+=1
            for k in range(4):
                board[k].pop(j)
                board[k].insert(0,0)
#4,5 번라인에 블록있다면 카운트하여 그만큼 팝,인서트 연산해주기             
def checkSpecial(board):
    count = 0
    for j in range(4,6):
        for i in range(4):
            if board[i][j] == 1:
                count+=1
                break
    
    for i in range(count):
        for j in range(4):
            board[j].pop()
            board[j].insert(0,0)
board_r = [[0]*10 for i in range(4)]
board_d = [[0]*4 for i in range(10)]


answer = 0
N = int(input())
#연산이 끝나고 타일갯수를 구하기위한 함수
def countTile():
    a = list(chain(*board_r)).count(1)
    b = list(chain(*board_d)).count(1)
    return a+b
    
for _ in range(N):
    type,x,y = map(int,input().split())
    putTile(type,x,y)
    board_d=rotate(board_d,0)
    tileMove(board_r)
    tileMove(board_d)
    checkLine(board_r)
    checkLine(board_d)
    checkSpecial(board_r)
    checkSpecial(board_d)
    board_d=rotate(board_d,1)

print(answer)
print(countTile())
