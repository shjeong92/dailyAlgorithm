import sys
input = sys.stdin.readline

T = int(input())

for x in range(T):
    #팀의 수
    N = int(input())
    data = list(map(int,input().split()))
    M = int(input())
    parent = [i for i in range(N+1)]
    
    graph = [[False]*(N+1) for _ in range(N+1)]
    # 첫 tc 5, 4 ,3, 2, 1
    #작년기록
    # 5는 4,3,2,1 이기고, 4는 3,2,1 이기고 3은 2,1 이기고 ..... 표시해주기.
    for i in range(N):
        for j in range(i+1,N):
            graph[data[i]][data[j]] = True
    #올해기록 바뀐부분 스왑해주기.
    for _ in range(M):
        a, b = map(int,input().split())
        graph[a][b],graph[b][a] = graph[b][a],graph[a][b]

    ranking = []
    #True 갯수가 같은 팀이 있다면 올바른 순위출력 불가능하다.
    for i in range(1,N+1):
        trueCount = 0
        for j in range(1,N+1):
            if graph[i][j] == True:
                trueCount += 1
        #이긴횟수와, 팀번호를 저장해준다.
        ranking.append([trueCount,i])
    ranking.sort(reverse = True)
    isPossible = True
    #만약 이긴횟수가 비슷한 팀이있다면 실패
    for i in range(len(ranking)-1):
        if ranking[i][0] == ranking[i+1][0]:
            isPossible = False
    
    if not isPossible:
        print('IMPOSSIBLE')
        continue
    
    for k in range(len(ranking)):
        print(ranking[k][1], end = ' ')
    print('')

