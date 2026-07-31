def solution(s):
    answer = []
    temp = s
    zero_count = 0
    change_count = 0
    
    while temp != "1":
        zero_count += temp.count("0")
        temp = temp.replace("0", "")
        temp = bin(len(temp))[2:]
        change_count += 1
    
    answer.append(change_count)
    answer.append(zero_count)
    return answer