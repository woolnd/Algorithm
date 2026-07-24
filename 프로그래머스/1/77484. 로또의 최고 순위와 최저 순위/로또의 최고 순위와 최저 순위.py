def solution(lottos, win_nums):
    answer = [6, 6]
    
    win_count = 0
    zero_count = 0
    
    for num in lottos:
        if num in win_nums:
            win_count += 1
        if num == 0:
            zero_count += 1
            
    answer[1] = 7 - win_count
    answer[0] = 7 - (win_count+zero_count)
    
    if answer[0] == 7:
        answer[0] = 6
        
    if answer[1] == 7:
        answer[1] = 6
    
    return answer