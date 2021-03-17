from bisect import bisect_left,bisect_right
def solution(N, stages):
    #정렬해주고
    stages.sort()
    #사전 초기화해주고
    memo = {i+1:0 for i in range(N)}
    #사람수구하고
    people = len(stages)
    #1번부터 N번까지 스테이지의 실패율구하기
    for i in range(1,N+1):
        #머물러있는사람 구하고
        val = bisect_right(stages,i)-bisect_left(stages,i)
        # 계산후 그사람만큼 사람수 감소
        if people != 0:
            memo[i] = val/people
            people -= val
        # 0 명이면 0
        else:
            memo[i] = 0
    # 실패율기준 내림차순, 스테이지 번호기준 오름차순 정렬.
    memo = sorted(memo.items(), key = lambda x : (-x[1],x[0]))
    return [i[0] for i in memo]
