def solution(t, p):
    answer = 0
    temp = ''
    
    length = len(p)
    
    for i in range(len(t)-length+1):
        if (i+length-1) <= len(t):
            
            temp = ''.join(t[j] for j in range(i, i+length))
                
            if int(p) >= int(temp):
                answer += 1
        temp = ''
    return answer