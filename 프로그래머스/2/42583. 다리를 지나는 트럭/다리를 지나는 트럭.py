def solution(bridge_length, weight, truck_weights):
    from collections import deque
    truck_weights.reverse()
    bridge = deque([0] * (bridge_length -1))
    bridge.appendleft(truck_weights.pop())
    ans, bridge_weight = 1,bridge[0]
    while bridge_weight:
        bridge_weight -= bridge.pop()
        if truck_weights and weight - bridge_weight >= truck_weights[-1]:
            bridge.appendleft(truck_weights.pop())
            bridge_weight += bridge[0]
        else:
            bridge.appendleft(0)
        ans +=1
    return ans
    
   