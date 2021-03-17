import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [list(map(str,input().rstrip().split())) for _ in range(N)]

wall = []
teachers = []
for i in range(N):
    for j in range(N):
        #벽을세울수 있는 좌표 저장
        if graph[i][j] =='X':
            wall.append([i,j])
        #선생님 좌표저장
        if graph[i][j] =='T':
            teachers.append([i,j])
#벽을 3개 세울 수 있는 모든 경우의수 구하기
candidates = list(combinations(wall,3))
#선생님이 학생을 발견하는지 체크
def check(c_graph,x,y,dir):
    #Right
    if dir == 0:
        while x < N:
            if c_graph[x][y] == 'S':
                return True
            if c_graph[x][y] == 'O':
                return False

            x += 1
    #Left
    if dir == 1:
        while 0 <= x:
            if c_graph[x][y] == 'S':
                return True
            if c_graph[x][y] == 'O':
                return False
            x -= 1
    #Up
    if dir == 2:
        while 0 <= y:
            if c_graph[x][y] == 'S':
                return True
            if c_graph[x][y] == 'O':
                return False
            y -= 1
    #Down
    if dir == 3:
        while y < N:
            if c_graph[x][y] == 'S':
                return True
            if c_graph[x][y] == 'O':
                return False   
            y += 1
    
    return False

result ='NO'
for candidate in candidates:
    #벽 세우기전 맵 복사하기.
    c_graph = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            c_graph[i][j] = graph[i][j]
    #벽세우기
    for cx, cy in candidate:
        c_graph[cx][cy] = 'O'
    temp = 'YES'
    for tx,ty in teachers:
        for i in range(4):
            if check(c_graph,tx,ty,i):
                temp = 'NO'
    #아무 학생도 안걸린경우 반복문 빠져나옴.
    if temp =='YES':
        result = 'YES'
        break

print(result)
    
    

    
