import sys
input = sys.stdin.readline

#세로방향 검사하기위해 90도 배열 90도 돌리기
def rotate(array):
    temp = [[0]*N for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            temp[i][j] = array[j][N-i-1]
    return temp

#한줄 한줄 입력 받으면서 길 체크하기.
def counter(array, i):
    c = [0 for _ in range(N)]
    for j in range(N-1):
        #만약 다음칸과의 차이가 1넘게나면 길이아니다.
        if abs(array[i][j] - array[i][j+1]) > 1:
            return 0
        #만약 오르막길이었을때.
        if array[i][j] < array[i][j+1]:
            temp = [0 for _ in range(N)]
            #이전길이 현재칸과 높이가같으며 길이가 L이 되는지 체크
            for k in range(L):
                #L길이만큼 돌 칸이없다.
                if j - k < 0:
                    return 0
                #L길이만큼 돌기전에 높이가 바뀐다 or 발판이 깔려있는데 또깔았다
                if array[i][j] != array[i][j - k] or c[j - k] != 0:
                    return 0
                #발판을 깔아준다
                temp[j - k] = 1
            c = temp
        #만약 내리막길이라면 한칸앞부터 길이 L 만큼검사
        elif array[i][j] > array[i][j+1]:
            temp = [0 for _ in range(N)]
            for k in range(L):
                #배열의 끝초과.
                if j + k + 1 >= N:
                    return 0
                #L길이 도달전 높이바뀌거나 이미 발판이깔려있으면 탈락
                if array[i][j+1] != array[i][j+k+1] or c[j+k+1] != 0:
                    return 0
                temp[j+k+1] = 1
            c = temp
    #모든단계를 무사히 통과하면 1
    return 1

answer = 0                
N, L = map(int,input().split())
#입력받은길
array = [list(map(int,input().split())) for _ in range(N)]
#90도회전한 길
r_array=rotate(array)

for i in range(N):
    answer += counter(array,i)
    answer += counter(r_array,i)
print(answer)
