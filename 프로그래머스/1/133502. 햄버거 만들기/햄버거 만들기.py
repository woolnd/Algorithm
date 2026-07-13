def solution(ingredient):
    answer = 0
    
    hamburger_stack = []
    
    for item in ingredient:
        hamburger_stack.append(item)
        
        if hamburger_stack[-4:] == [1,2,3,1]:
            for _ in range(4):
                hamburger_stack.pop()
            
            answer += 1
    return answer