def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            prev_i = stack.pop()
            answer[prev_i] = i - prev_i
        stack.append(i)
        
    last_index = len(prices) - 1
    
    while stack:
        index = stack.pop()
        answer[index] = last_index - index
        
    return answer