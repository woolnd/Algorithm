def solution(board, h, w):
    answer = 0
    
    dh = [1, -1, 0, 0]
    dw = [0, 0, -1, 1]
    
    color = board[h][w]
    
    for i in range(4):
        h_check = dh[i] + h
        w_check = dw[i] + w
        
        if h_check < 0 or h_check >= len(board) or w_check < 0 or w_check >= len(board[0]):
            continue
        
        if color == board[h_check][w_check]:
            answer += 1
    
    return answer