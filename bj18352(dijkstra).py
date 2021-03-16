import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
N, M, K, X = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for _ in range(M):
    a, b = map(int,input().split())
    #node, distance
    graph[a].append([b,1])
#start = X
#distance, node 거리우선순이 다익스트라 알고리즘활용 간선간 거리가 모두 1일때는 BFS로 푸는게 빠르다. 다익스트라 복습용 코드
q = [[1,X]]
distance[X] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist < distance[now]:
        continue
    
    for i in graph[now]:
        cost = i[1] + distance[now]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,[cost,i[0]])
answer = []
for i in range(1,N+1):
    if distance[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    for i in answer:
        print(i)