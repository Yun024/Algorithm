from datetime import datetime

def solution(plans):
    
    plans = sorted(plans, key=lambda x: x[1])
    stack = []
    answer = []

    cur_name, cur_start, cur_duration = plans.pop(0)
    cur_time = datetime.strptime(cur_start, "%H:%M")
    cur_duration = int(cur_duration)

    while plans:
        next_name, next_start, next_duration = plans[0]
        next_time = datetime.strptime(next_start, "%H:%M")

        gap = int((next_time - cur_time).total_seconds() // 60)

        if gap < cur_duration:
            stack.append([cur_name, cur_duration - gap])
        else:
            answer.append(cur_name)
            remain = gap - cur_duration

            while remain and stack:
                stack_name, stack_time = stack.pop()
                if remain >= stack_time:
                    answer.append(stack_name)
                    remain -= stack_time
                else:
                    stack.append([stack_name, stack_time - remain])
                    break

        cur_name, cur_start, cur_duration = plans.pop(0)
        cur_time = datetime.strptime(cur_start, "%H:%M")
        cur_duration = int(cur_duration)

    answer.append(cur_name)

    while stack:
        answer.append(stack.pop()[0])

    return answer
