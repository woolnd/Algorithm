def solution(board, moves):
    answer = 0
    
    basket = []
    
    board_len = len(board)
    top_row = {j: -1 for j in range(board_len)}

    for i in range(board_len):
        for j in range(board_len):
            if top_row[j] == -1 and board[i][j] != 0:
                top_row[j] = i
    
    for move in moves:
        col = move - 1
        if top_row[col] == -1:
            continue
        
        row = top_row[col]
        value = board[row][col]
        
        if basket and basket[-1] == value:
            basket.pop()
            answer += 2
        else:
            basket.append(value)
        
        if row + 1 < board_len:
            top_row[col] = row + 1
        else:
            top_row[col] = -1
        
    return answer