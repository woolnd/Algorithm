def solution(s):
    answer = ''
    
    eng_dict = {
        'zero': '0',
        'one': '1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    
    temp = ''
    
    for c in s:
        if temp in eng_dict.keys():
            answer += eng_dict[temp]
            temp = ''
            
        if c.isdigit():
            answer += c
        else:
            temp += c
            continue
        
    if temp in eng_dict.keys():
        answer += eng_dict[temp]
        
    return int(answer)