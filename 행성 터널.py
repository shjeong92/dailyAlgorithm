import sys
input = sys.stdin.readline
#죄표가 세개..
#첫 풀이때 이중 포문을 돌며 2차원 배열에 각노드간의 거리를 모두기록하여 크루스칼 알고리즘을 이용하였더니 75%쯤에서 메모리초과가 났다.
#x따로 y따로 z따로 정렬해도 무조건 풀릴 수 있다는점을 전혀 생각지 못했다. N^2 - > 3*N 으로 줄어들어서 풀 수 있었다.
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = parent[a]
    b = parent[b]

    if a != b:
        parent[b] = a

#행성 갯수
N = int(input())
parent=[i for i in range(N)]
x = []
y = []
z = []

for i in range(N):
    a,b,c = map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

edges = []
result = 0
for i in range(N-1):
    edges.append((abs(x[i+1][0]-x[i][0]),x[i][1],x[i+1][1]))
    edges.append((abs(y[i+1][0]-y[i][0]),y[i][1],y[i+1][1]))
    edges.append((abs(z[i+1][0]-z[i][0]),z[i][1],z[i+1][1]))
#짧은거리 먼저 묶어주기위하여
edges.sort()
for edge in edges:
    cost, a, b = edge
    #사이클이 생기지 않는다면 합치기
    if find(parent,a) != find(parent,b):
        union(parent, a, b)
        result += cost
print(result)
