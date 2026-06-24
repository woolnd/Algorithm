def solution(keymap, targets):
    answer = []
    
    key_dict = {}
    
    for keys in keymap:
        for index, char in enumerate(keys):            
            if char in key_dict:
                key_dict[char] = min(key_dict[char], index + 1)
            else:
                key_dict[char] = index + 1
            

    for target in targets:
        count = 0
        for char in target:
            if char in key_dict:
                count += key_dict[char]
            else:
                count = -1
                break
                
        answer.append(count)
        
    return answer