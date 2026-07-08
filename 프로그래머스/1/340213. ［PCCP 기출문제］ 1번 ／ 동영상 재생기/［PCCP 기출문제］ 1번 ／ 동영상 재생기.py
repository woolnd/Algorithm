def solution(video_len, pos, op_start, op_end, commands):
    
    video_split = video_len.split(":")
    v_h = int(video_split[0]) * 60
    v_m = int(video_split[1])
    v_s = v_h + v_m
    
    pos_split = pos.split(":")
    h = int(pos_split[0]) * 60
    m = int(pos_split[1])
    s = h + m
    
    op_start_split = op_start.split(":")
    op_s_h = int(op_start_split[0]) * 60
    op_s_m = int(op_start_split[1])
    op_s_s = op_s_h + op_s_m
    
    op_end_split = op_end.split(":")
    op_e_h = int(op_end_split[0]) * 60
    op_e_m = int(op_end_split[1])
    op_e_s = op_e_h + op_e_m
    
    
    for command in commands:
        if (op_s_s<=s) and (s<=op_e_s):
            s = op_e_s
        
        if command == 'next':
            s += 10
            
            if s >= v_s:
                s = v_s
                
        elif command == 'prev':
            s -= 10

            if s <= 0:
                s = 0
    
    if (op_s_s<=s) and (s<=op_e_s):
        s = op_e_s
            
    if s  >= 60:
        h = s // 60
        m = s % 60
        
        result_h = f"{h}" if h>= 10 else f"0{h}"
        result_m = f"{m}" if m>= 10 else f"0{m}"
    else:
        result_h = "00"
        result_m = f"{s}" if s >= 10 else f"0{s}"
    return f"{result_h}:{result_m}"