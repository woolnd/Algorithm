def solution(s):
    answer = 0
    same = 0
    diff = 0
    x = s[0]
    
    for i in range(len(s)):
        if x == s[i]:
            same += 1
        if x != s[i]:
            diff += 1
        
        if same == diff:
            if i+1 < len(s):
                x = s[i+1]
                answer += 1
            else:
                break
        
    return answer+1