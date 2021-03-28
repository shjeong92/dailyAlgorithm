import sys,copy
input = sys.stdin.readline
#첫 시도때 리스트로 연결을 표현하였을때 복사, 와 check 함수에서 엄청난 시간이 걸려 0%도 못가보고 시간초과하엿고, 2차원배열로 연결을 표현하니 통과하였다
#python3 로는 통과못하였고 pypy3로는 통과하엿다
N, M, H = map(int, input().split())
board = [[0 for i in range(H+1)] for i in range(N+1)]

for i in range(M):
    a, b = map(int,input().split())
    #a번째줄에 b 와 b+1 가 연결됨을 표시해주기
    board[b][a] = b+1
    board[b+1][a] = b

def check(board):
    #사다리 탔을때 자기자신 안나오면 리턴 0
    for i in range(1,N+1):
        now = i
        d = 1
        while d <= H:
            if board[now][d] != 0:
                
                now = board[now][d]
            d += 1
        if i != now:
            return 0
    #끝까지 통과하면 성공.
    return 1
answer = 1e9
def dfs(board,depth):
    global answer
    #만약에 통과된다면 깊이 더 작은 값으로 업데이트 시켜주기
    if check(board):
        answer = min(answer,depth)
        return
    #깊이가 3이거나, answer보다 크다면 탈출하기
    if depth == 3 or depth>=answer:
        return
    #보드에 영향가지않게 복사하기.
    board = copy.deepcopy(board)
    #보드 전체를 탐색
    for i in range(1,N):
        for j in range(1,H+1):
            #만약에 다리를 놓을 수 있다면 놓은다음에
            if board[i][j] == 0 and board[i+1][j] == 0:
                board[i][j] = i + 1
                board[i+1][j] = i
                #dfs 
                dfs(board,depth+1)
                #다리 끊어줌 결과적으로 모든 다리를 놓을 수 있는 NC1 부터 NC3까지 모두 탐색할 수 있다. 
                board[i][j] = 0 
                board[i+1][j] = 0
                
    
dfs(board,0)
print(answer if answer!= 1e9 else -1)
