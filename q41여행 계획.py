import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[0]*(N+1) for _  in range(N+1)]
temp = [list(map(int,input().split())) for _ in range(N)]
#한칸 늘려서 1번부터시작하는 번호 맞춰주기.
for i in range(N):
    graph[i+1][1:] = temp[i]

parent = [i for i in range(N+1)]

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a = parent[a]
    b = parent[b]
    if a != b:
        parent[b] = a

for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] == 1:
            union(parent, i, j)

que = list(map(int,input().split()))

answer = 'YES'
tmp = None
for i in que:
    if tmp == None:
        tmp = find(parent,i)
    
    else:
        if tmp != find(parent,i):
            answer = 'NO'
print(answer)
