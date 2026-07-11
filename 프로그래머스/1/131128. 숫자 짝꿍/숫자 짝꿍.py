def solution(X, Y):
    answer = []
    
    for i in range(9, -1, -1):
        char = str(i)
        
        count = min(X.count(char), Y.count(char))
        answer.append(char * count)
        
    result = ''.join(answer)
    
    if result == '':
        return '-1'
    
    if result[0] == '0':
        return '0'
        
    return result
     