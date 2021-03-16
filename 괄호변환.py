def solution(p):
    #v 가 빈 문자열일때 빠져나가줘야함.
    if p == '':
        return ''
    oParen = 0
    cParen = 0
    idx = 0
    isPerfect = True
    pCheck = 0
    for i in range(len(p)):
        #괄호 열릴때 pCheck +=1 닫힐때 -=1 해준다 만약 이 pCheck이 음수값으로 내려간다면 불완전한 괄호이다.
        if p[i] == '(':
            oParen +=1
            pCheck += 1
        elif p[i] == ')':
            cParen +=1
            pCheck -= 1
        if pCheck<0:
            isPerfect = False
        # 균형잡힌문자열로 자르기위해 idx 값 저장.
        if oParen == cParen:
            idx = i
            break
    u = p[:idx+1]
    v = p[idx+1:]
    
    if isPerfect:
        return u + solution(v)
    #괄호방향을 뒤집는다는 말을 리스트로 만들어서 리버스 시킨다음 붙이라는 말인줄 착각하고 해맸다..
    else:
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i]= ')'
            else:
                u[i] ='('
        u = ''.join(u)
        return '(' + solution(v) + ')' + u
