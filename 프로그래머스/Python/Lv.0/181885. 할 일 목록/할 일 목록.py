def solution(todo_list, finished):
    return [j for j,i in zip(todo_list,finished) if i ==False]
    