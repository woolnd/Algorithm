from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_queue = deque()
    curr_time = 0
    curr_weight = 0
    wait_truck = deque(truck_weights)
    
    while bridge_queue or wait_truck:
        curr_time += 1
        
        if bridge_queue and bridge_queue[0][1] == curr_time:
            exit_weight, _ = bridge_queue.popleft()
            curr_weight -= exit_weight
            
        
        if wait_truck:
            next_weight = wait_truck[0]
            
            if curr_weight + next_weight <= weight:
                wait_truck.popleft()
                curr_weight += next_weight
                exit_time = curr_time + bridge_length
                bridge_queue.append((next_weight, exit_time))
    
    return curr_time