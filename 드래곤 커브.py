import sys
input = sys.stdin.readline
#row, col 반대로 넣는 바보짓함.. 문제를 잘 읽어보자
N = int(input())
visited = [[0]*101 for i in range(101)]
dir = []
dx = [0,-1,0,1]
dy = [1,0,-1,0]
#방향별 드래곤커브 10세대까지 만들어놓기
for i in range(4):
    temp = [i]
    for j in range(10):
        l = len(temp)
        for k in range(l-1,-1,-1):
            temp.append((temp[k]+1)%4)
    dir.append(temp)


for _ in range(N):
    y, x, d, gen = map(int,input().split())
    visited[x][y] = 1
    #N 세대의 방향좌표길이는 2의 N승과같음
    for i in range(2**gen):
        nx, ny = x + dx[dir[d][i]], y + dy[dir[d][i]]
        visited[nx][ny] = 1
        x, y = nx, ny
answer = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1]:
            answer += 1
print(answer)
