import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))
arr = []
#기존 길이만 구할 수 있는 LIS에서 기록을 저장하여 실제 배열을 구하기위한 리스트
# [인덱스, 값]
history = []
MAX = None
for i in range(N):
    if MAX == None:
        #첫값은 그냥 넣기.
        arr.append(data[i])
        history.append([i,data[i]])
        #최댓값 초기화.
        MAX = data[i]
    #첫값이 아닐경우
    else:
        #뒤에 붙이는 값이 마지막 값보다 클경우
        if data[i] > MAX:
            #길이구하기용 LIS에 붙이고,
            arr.append(data[i])
            #레알 배열구하기위한 히스토리도 남기고
            history.append([len(arr)-1,data[i]])
            #최댓값 갱신해줌
            MAX = data[i]
        #만약에 끝값보다 작다면 
        elif data[i] <= MAX:
            #lowerbound 써서 그위치에 값 바꿔넣어주고, 히스토리에 저장해준다.
            start = 0
            end = len(arr)-1

            while start < end:
                mid = (start + end) // 2
                if arr[mid] >= data[i]:
                    end = mid
                else:
                    start = mid + 1
            
            arr[start] = data[i]
            history.append([start,data[i]])
            MAX = arr[-1]

stack = []        
t = len(arr)-1
#뒤에서부터 차례대로, 만들어진 짝퉁LIS 배열의 인덱스 찾고 스택에 넣어주기.
for i in range(N-1,-1,-1):
    if history[i][0] == t:
        stack.append(history[i][1])
        t -= 1
#정답 출력.
print(len(stack))
while stack:
    print(stack.pop(),end=' ')
