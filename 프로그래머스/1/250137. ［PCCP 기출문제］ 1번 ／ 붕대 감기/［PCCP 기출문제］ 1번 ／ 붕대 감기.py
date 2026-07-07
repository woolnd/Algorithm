def solution(bandage, health, attacks):
    
    start = 1
    hp = health
    
    for i, j in attacks:
        hp += ((i-start) * bandage[1]) + ((i-start) // bandage[0] * bandage[2])
        if hp >= health:
            hp = health
        hp -= j
        
        if hp <= 0:
            hp = -1
            break
            
        start = i + 1
    
    return hp