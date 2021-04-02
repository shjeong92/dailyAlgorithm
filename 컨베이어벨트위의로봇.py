import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int,input().split())
belt = list(map(int,input().split()))
pos = [0]*2*N
time = 0
while belt.count(0) < K:
    #1단계부터 시작한다.
    time+=1
    #일단 한바퀴 회전시킨다.
    belt.insert(0,belt.pop())
    pos.insert(0,pos.pop())
    #내려가는칸 내려주고
    pos[N-1] = 0
    #로봇이 있는칸 로봇 들어간시간별로 오름차순정렬하여
    for (r, i) in sorted([(pos[i],i) for i in range(2*N) if pos[i] > 0]):
        #순서대로 한칸앞에 비어있고, 밸트내구도가 남아있으면 이동시키고 내구도감소시켜준다.
        if pos[i+1] == 0 and belt[i+1] > 0:
            pos[i] = 0
            pos[i+1] = r
            belt[i+1] -= 1
    #이동후 내리는칸 정리해준다. 
    pos[N-1] = 0
    #올리는칸 비어있으면 로봇넣어준다. 로벗번호는 시간.
    if belt[0] > 0:
        belt[0] -= 1
        pos[0] = time  
print(time)

