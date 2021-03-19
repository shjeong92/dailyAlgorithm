def solution(n, results):
    #그래프 초기화
    graph = [[None] * (n+1) for _ in range(n+1)]
    for x,y in results:
        #x는 y에게 이김
        graph[x][y] = True
    #플로이드 워셜 알고리즘
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                #만약 i가 k에게 이기고 k가 j에게 이겼다면 i는 j를 이긴거다
                if graph[i][k] == True and graph[k][j] ==True:
                    graph[i][j] = True
                    
    answer = 0
    for i in range(1,n+1):
        cnt = 0 
        for j in range(1,n+1):
            #선수i vs j 에서 한쪽이라도 True 라면 승패 구분이 가능한것.
            if graph[i][j] == True or graph[j][i] == True:
                cnt +=1
        #정확한 순위를 알려면 사람수-1의 경기기록이 필요.
        if cnt == n-1:
            answer+=1
    
    return answer
