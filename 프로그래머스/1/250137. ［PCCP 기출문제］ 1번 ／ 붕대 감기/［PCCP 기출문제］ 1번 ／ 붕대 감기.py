def solution(bandage, health, attacks):
    
    last_time = 0
    cur_health = health
    
    for attack_time, attack_damage in attacks:
        gap = attack_time - last_time - 1
        success = gap * bandage[1]
        
        cur_health = min(cur_health + success, health)
        
        if gap // bandage[0] >= 1:
            cur_health += bandage[2] * (gap // bandage[0])
            cur_health = min(cur_health, health)
            
        cur_health -= attack_damage
        
        if cur_health <= 0: 
            cur_health = -1
            break
        
        
        last_time = attack_time
            
    return -1 if cur_health <= 0 else cur_health