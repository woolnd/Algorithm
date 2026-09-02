def solution(records):
    uid_to_name = {}
    history = []   
    
    for record in records:
        parts = record.split(" ")
        status = parts[0]
        id = parts[1]
        
        
        if status == "Leave":
            history.append((status, id))
        else:
            name = parts[2]
            uid_to_name[id] = name
            
            if status == "Enter":
                history.append((status, id))
            else:
                uid_to_name[id] = name
                history.append((status, id))
        
    
    answer = []
    for record in history:
        status = record[0]
        id = record[1]
        name = uid_to_name[id]
        
        if status == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        elif status == "Leave":
            answer.append(f"{name}님이 나갔습니다.")
        
    return answer