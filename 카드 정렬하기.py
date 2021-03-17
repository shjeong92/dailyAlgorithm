import sys
import heapq
input = sys.stdin.readline
N = int(input())
cards = []
#최소힙써서 알아서 정렬시키기.
for _ in range(N):
    heapq.heappush(cards,int(input()))
answer = 0
#카드없어질때까지 두장뽑아서 더하고 그값다시 정렬된채로 넣고 카드없어질떄까지 반복
while cards:
    if cards:
        a = heapq.heappop(cards)
    else:
        break
    if cards:
        b = heapq.heappop(cards)
    else:
        break

    answer += a+b
    heapq.heappush(cards,a+b)
print(answer)

