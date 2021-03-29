import sys
from itertools import chain
input = sys.stdin.readline

R, C, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(3)]
#세로 정렬하기위해 배열 회전시키기.
def rotate(arr,dir):
    h = len(arr)
    w = len(arr[0])
    temp = [[0]*h for _ in range(w)]
    if dir =='L':
        for i in range(h):
            for j in range(w):
                temp[w-j-1][i] = arr[i][j]
        return temp
    elif dir == 'R':
        for i in range(h):
            for j in range(w):
                temp[j][h-i-1] = arr[i][j]

    return temp

time = 0
#정렬 함수
def sorting(arr):
    new_arr = []
    max_len = 0
    result = []
    
    for i in range(len(arr)):
        #각 행에 있는 숫자가 몇번나오나 사전으로 체크하기
        temp = {}
        for num in arr[i]:
            #숫자가 0이 아닐경우만 사전에 등록해주기.
            if num != 0:
                if num in temp:
                    temp[num] += 1
                else:
                    temp[num] = 1
        #사전 정렬하기
        temp = sorted(temp.items(),key = lambda x:(x[1],x[0]))
        #숫자 등장횟수 정렬된것 new_arr에 넣기
        new_arr.append(temp)
        #제일 긴 행만큼 0,0 추가해줘야하므로 max_len 갱신해주기
        if len(temp) > max_len:
            max_len = len(temp)
    #new_arr 처음부터 끝가지돌면서 0,0채워주기
    for li in new_arr:
        while len(li) < max_len:
            li.append((0,0))
        #chain으로 이어준다음 결과에 추가하기
        result.append(list(chain(*li)))


    return result

err = 0
#100초까지 돌리기~
while time <101:
    '''
    1 1 1     1 3  R = 3, C = 3 일경우
    1 1 1  => 1 3  indexerror 생기는거 방지하기위해 예외처리 해주기
    1 1 1     1 3  
    '''
    try:
        if arr[R-1][C-1] == K:
            break
    except:
        err =1
    #열길이
    width = len(arr[0])
    #행길이
    height = len(arr)
    #행길이가 열길이보다 크거나 같을경우 행정렬
    if height >= width:
        arr = sorting(arr)
    #그렇지 않을경우 열정렬
    else:
        # 배열을 왼쪽으로 회전시킨다음
        arr = rotate(arr,"L")
        # 행정렬 후
        arr = sorting(arr)
        # 다시 오른쪽으로 돌리는 방식으로 
        arr = rotate(arr,"R")
    time+=1
#100초 안넘으면 초찍고 넘으면 -1 찍어주기
print(time if time != 101 else -1 )
