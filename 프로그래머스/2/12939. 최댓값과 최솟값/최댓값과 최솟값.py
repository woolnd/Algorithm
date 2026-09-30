def solution(s):
    
    num_list = list(map(int, s.split(" ")))
    num_list = sorted(num_list)

    return f"{num_list[0]} {num_list[-1]}"