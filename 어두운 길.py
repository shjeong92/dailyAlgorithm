import sys
import heapq
'''
N개의 마을과 M개의 도로로 이루어진마을 집은 0번부터 N-1번까지의 번호로 구분됨
특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와동일

가로등을 일부 비활성화하고 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 함.
=> 최소 신장트리
'''


'''
입력
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''
input = sys.stdin.readline
N, M = map(int,input().split())
parent = [i for i in range(N)]
q = []

total = 0
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = parent[a]
    b = parent[b]
    if a != b:
        parent[b] = a

for _ in range(M):
    a, b, cost = map(int,input().split())
    heapq.heappush(q,(cost,a,b))
    #모든 가로등을 켤때의 금액 구하기
    total += cost
    
answer = 0
while q:

    cost, a, b = heapq.heappop(q)
    #싸이클이 안생긴다면 연결후 가격 더하기
    if find(parent,a) != find(parent,b):
        answer += cost
        union(parent,a,b)
#총 가격 - 가로등 비활성후 가격 = 절약한 금액
print(total - answer)
