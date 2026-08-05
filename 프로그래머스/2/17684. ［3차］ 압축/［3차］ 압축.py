def solution(msg):
    answer = []
    
    dic = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z')+1)}
    
    i = 0
    while i < len(msg):
        w = msg[i]
        j = i + 1
        
        while j < len(msg) and (w + msg[j]) in dic:
            w += msg[j]
            j += 1
        
        answer.append(dic[w])
        
        if j < len(msg):
            dic[w+msg[j]] = len(dic) + 1
    
        i = j
    return answer