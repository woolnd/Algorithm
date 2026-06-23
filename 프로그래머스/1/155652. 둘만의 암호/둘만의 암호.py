def solution(s, skip, index):
    answer = ''
    
    for char in s:
        moved = 0  
        curr = char
        
        while moved < index:
            if curr == "z":
                curr = "a"
            else:
                curr = chr(ord(curr) + 1)
            
            if curr in skip:
                continue
            else:
                moved += 1  
            
        answer += curr

    return answer