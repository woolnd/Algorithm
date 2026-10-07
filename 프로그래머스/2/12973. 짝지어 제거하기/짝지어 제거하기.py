def solution(s):
    char_stack = []
    
    for char in s:
        if len(char_stack) != 0:
            if char_stack[-1] != char:
                char_stack.append(char)    
            else:
                char_stack.pop()
        else:
            char_stack.append(char)
    
    if len(char_stack) == 0:
        return 1
    else:
        return 0