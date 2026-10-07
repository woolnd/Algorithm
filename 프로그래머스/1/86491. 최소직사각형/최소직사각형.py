def solution(sizes):
    max_w = 0
    max_h = 0
    
    for size in sizes:
        if size[0] >= size[1]:
            max_w = max(max_w, size[0])
            max_h = max(max_h, size[1])
        else:
            max_w = max(max_w, size[1])
            max_h = max(max_h, size[0])
    
    return max_w * max_h