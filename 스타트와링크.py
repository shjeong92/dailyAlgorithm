import sys
from itertools import combinations as combi
input = sys.stdin.readline
N = int(input())
#팀 0~N-1번
candidates = [i for i in range(N)]
#i와j가 만나면 얻는점수 데이타
data = [list(map(int,input().split())) for _ in range(N)]
answer = int(1e9)
#팀을 만들수 있는 모든 경우 li vs temp
for li in list(combi(candidates,len(candidates)//2)):
    temp = []
    for candi in candidates:
        if candi not in li:
            temp.append(candi)
    # print(li,temp)
    start = 0
    link = 0
    #start 팀과 link팀의 점수를 구하고
    for i in range(len(li)):
        for j in range(len(li)):
            if i != j:
                start += data[li[i]][li[j]]
                link += data[temp[i]][temp[j]]
    #초기화해준다 최소값으로
    answer = min(abs(start-link), answer)
print(answer)
