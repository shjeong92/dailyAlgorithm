import sys
from collections import deque
input = sys.stdin.readline
#톱니바키를 방향에 맞게 돌려주는 함수.
def turn(deque,dir):
    #오른쪽으로 돌리기
    if dir == 1:
        a = deque.pop()
        deque.insert(0,a)
    #왼쪽으로 돌리기
    elif dir == -1:
        a = deque.popleft()
        deque.append(a)

def roll(gears,gearnum,dir):
    #돌릴 톱니바퀴들의 정보를 담은 리스트.
    turnList = [(gearnum,dir)]
    #왼쪽방향 탐색하기.
    if gearnum > 0:
        #비교할 기어
        rightGear = gears[gearnum]
        #방향
        d = dir
        
        for i in range(gearnum-1,-1,-1):
            #비교할 기어의 왼쪽과 선택된기어의 오른쪽의 기어의 극이 다를경우 리스트에 회전방향바꿔서 추가
            if rightGear[6] != gears[i][2]:
                d = -d
                turnList.append((i,d))
                rightGear = gears[i]
            #만약 같다면 반복문종료.
            else:
                break
    if gearnum <3:
        leftGear = gears[gearnum]
        d = dir
        for i in range(gearnum+1,4):
            #비교할 기어의 오른쪽과 선택된기어의 왼쪽쪽의 기어의 극이 다를경우 리스트에 회전방향바꿔서 추가
            if leftGear[2] != gears[i][6]:
                d = -d
                turnList.append((i,d))
                leftGear = gears[i]
            #같다면 반복문 종료
            else:
                break
    #돌려야할 톱니바퀴 돌려주기.
    if turnList:
        for gearnum, dir in turnList:
            turn(gears[gearnum],dir)

#기어정보 입력받기.
gears = [deque(list(input().rstrip())) for _ in range(4)]
#돌릴횟수 입력받기
K = int(input())
for _ in range(K):
    #돌릴기어번호, 방향
    gearnum, dir = map(int,input().split())
    #돌려돌려~
    roll(gears,gearnum-1,dir)

gVal = [1, 2, 4, 8]
answer = 0
#모든 기어를 체크하며 북족방향이 1일경우 해당 점수를 정답에 더해줌
for i in range(4):
    if gears[i][0] == '1':
        answer+=gVal[i]
print(answer)






