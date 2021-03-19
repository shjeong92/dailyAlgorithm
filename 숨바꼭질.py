import sys
import heapq
input = sys.stdin.readline

N, M = map(int,input().split())
INF = 1e9
distance = [INF]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))


start = 1
distance[start] = 0
#cost, node
q = [(0,start)]

while q:
    
    dist, now = heapq.heappop(q)
    #다른곳을 거쳐가는것보다 그냥가는게 빠른경우 패스.
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))


MAX = max(distance[1:])
num = INF
d = MAX
count = 0
for i in range(N+1):
    if distance[i] == d:
        if i < num:
            num = i
        count += 1
print(num,d,count)
