from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int,input().split())

graph = [[]for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)

q = deque([X])
visited[X] = 0

while q:
    start = q.popleft()

    for node in graph[start]:
        if visited[node] == False:
            visited[node] = visited[start] + 1
            q.append(node)

answer = []

for i in range(1,N+1):
    if visited[i] == K:
        answer.append(i)
if not answer:
    print(-1)
else:
    for i in answer:
        print(i)


