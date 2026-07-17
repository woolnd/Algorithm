def solution(id_list, report, k):
    answer = []
    
    id_dict = {}
    report_dict = {}
    report_list = []
    
    for index, id in enumerate(id_list):
        id_dict[id] = index
        report_list.append([])
        answer.append(0)
    
    for info in report:
        s_info = info.split(" ")
        a_id = s_info[0]
        b_id = s_info[1]
        
        if b_id in report_list[id_dict[a_id]]:
            continue
        
        if b_id in report_dict.keys():
            report_dict[b_id] += 1
        else:
            report_dict[b_id] = 1
        
        report_list[id_dict[a_id]].append(b_id)
        
    for i in range(len(report_list)):
        for j in report_list[i]:
            if report_dict[j] >= k:
                answer[i] += 1

    return answer