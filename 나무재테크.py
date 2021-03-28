import sys,copy
input = sys.stdin.readline
N, M, K = map(int,input().split())
e_year = [list(map(int,input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
energy = [[5]*N for _ in range(N)]
#8방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(M):
    x, y, years = map(int,input().split())
    #나무리스트에 나무나이 입력
    trees[x-1][y-1].append(years)
def spring_summer(trees):
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                #어린나무먼저 처리하기위해 정렬
                trees[i][j].sort()
                #살아있는나무담을 temp_tree, dead_tree 죽은나무가 영양분이된값
                temp_tree,dead_tree =[], 0
                for age in trees[i][j]:
                    if age <= energy[i][j]:
                        energy[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                    else:
                        dead_tree += age//2
                energy[i][j] += dead_tree
                trees[i][j] = []
                #살아있는 나무리스트 갱신
                trees[i][j].extend(temp_tree)
def fall(trees):
    
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                #나무의 나이가 5의 배수이면 퍼져나가야함
                for age in trees[i][j]:
                    if age % 5 == 0:
                        for dir in range(8):
                            nx = i + dx[dir]
                            ny = j + dy[dir]
                            #맵안이라면 1살짜리나무 추가해주기
                            if 0<= nx < N and 0 <= ny < N :
                                trees[nx][ny].append(1)
    
def winter():
    #각 칸별 영양소 보충해주기
    for i in range(N):
        for j in range(N):
            energy[i][j] += e_year[i][j]

#K 년동안 반복
for _ in range(K):
    spring_summer(trees)
    fall(trees)
    winter()
answer = 0
#나무수 구하기
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            for v in trees[i][j]:
                if v!=0:
                    answer += 1

print(answer)

