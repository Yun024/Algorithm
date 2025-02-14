def solution(order):
    sub = []
    main = [i+1 for i in range(len(order))]
    main.reverse()
    order.reverse()
    ans = 0
    while order:
        if not main and sub[-1] != order[-1]:
            return ans
        elif sub and order[-1] == sub[-1]: 
            order.pop()
            sub.pop()
            ans +=1
        elif order[-1] == main[-1]:
            order.pop()
            main.pop()
            ans +=1
        else:
            sub.append(main.pop())
    return ans