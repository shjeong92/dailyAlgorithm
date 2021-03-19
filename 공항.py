import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
#두 원소가 속한 집합 합치기.
def union(parent, a, b):
    a = parent[a]
    b = parent[b]

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
result = 0

for _ in range(P):
    #현재 비행기의 탑승구의 루트 확인.
    data = find(parent,int(input()))
    #탑승구 루트 0까지 갈경우는 게이트 1반게이트까지 꽉찼을경우이므로 조건문탈출.
    if data == 0:
        break
    union(parent,data, data-1)
    result += 1

print(result)
