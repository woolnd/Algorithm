def solution(mats, park):
    answer = -1
    
    rows = len(park)
    cols = len(park[0])
    
    dp = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if park[i][j] != "-1":
                dp[i][j] = 0
            else:
                
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
                up_left = dp[i-1][j-1] if(i > 0) and (j > 0) else 0
                
                dp[i][j] = min(up, left, up_left) + 1
            
            if dp[i][j] in mats:
                answer = max(answer, dp[i][j])
     
    return answer