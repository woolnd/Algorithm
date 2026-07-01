def solution(schedules, timelogs, startday):
    answer = 0
    
    weekday_flags = []
    for col in range(7):
        day_of_week = (startday - 1 + col) % 7 + 1
        weekday_flags.append(day_of_week not in (6, 7))
        
    for i, log in enumerate(timelogs):
            h, m = divmod(schedules[i], 100)
            limit_minutes = h * 60 + m + 10
            limit = (limit_minutes // 60) * 100 + (limit_minutes % 60)
            
            time_flag = True
            for j, time in enumerate(log):
                if weekday_flags[j] and time > limit:
                    time_flag = False
                    break
            
            if time_flag:
                answer += 1
                    
                
    return answer