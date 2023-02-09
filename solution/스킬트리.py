def solution(skill, skill_trees):
    answer, skill_tree = 0, [] 
    for st in skill_trees:
        string = ""
        for s in st:
            if s in skill:
                string += s
        skill_tree.append(string)
    
    for st in skill_tree:
        for i in range(len(st)):
            if skill[i] != st[i]:
                break
        else:
            answer += 1
    
    return answer