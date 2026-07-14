def solution(survey, choices):
    answer = ''
    
    p_dict = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    
    for index, i in enumerate(survey):
        
        if choices[index] < 4:
            p_dict[i[0]] += 4-choices[index]
        elif choices[index] > 4:    
            p_dict[i[1]] += choices[index]-4
    
    for i in range(0,8,2):
        a = list(p_dict.keys())[i]
        b = list(p_dict.keys())[i+1]
        
        if p_dict[a] >= p_dict[b]:
            answer += a
        else:
            answer += b
        
    return answer
