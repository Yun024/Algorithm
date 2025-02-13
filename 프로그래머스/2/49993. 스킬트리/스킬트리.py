def solution(skill, skill_trees):
    ans = []
    for skill_tree in skill_trees:
        temp = ""
        for sk in skill_tree:
            if sk in skill:
                temp += sk
        if skill.startswith(temp):
            ans.append(temp)
            
    return len(ans)