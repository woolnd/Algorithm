def solution(new_id):
    temp = new_id
    
    temp = temp.lower()
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789-_."

    temp = ''.join(ch for ch in temp if ch in allowed)
    
    prev = ''
    result = ''
    
    for ch in temp:
        if ch == '.' and prev == '.':
            continue
        result += ch
        prev = ch
    
    if len(result) > 0 and '.' in result[0]:
        result = result[1:]
    
    if len(result) > 0 and '.' in result[-1]:
        result = result[:-1]
        
    if len(result) == 0:
        result += 'a'
        
    if len(result) >= 16:
        result = result[:15]
        if '.' in result[0]:
            result = result[1:]
        if '.' in result[-1]:
            result = result[:-1]
    
    while len(result) <= 2:
        result += result[-1]
        
    return result