def solution(n):
    a = "수"
    b = "박"
    flag = True
    answer = ""
    for _ in range(1, n+1):
        if flag:
            answer += a
            flag = False
        else:
            answer += b
            flag = True
            
    return answer