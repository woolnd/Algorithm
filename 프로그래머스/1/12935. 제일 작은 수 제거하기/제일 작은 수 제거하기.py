def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        answer = []
        min_num = min(arr)
        
        for i in arr:
            if i != min_num:
                answer.append(i)
    return answer