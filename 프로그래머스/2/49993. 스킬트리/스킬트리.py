def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        if check(i, skill):
            answer += 1
    return answer

def check(tree, skill):
    flag = False
    for s in range(len(skill)-1, -1, -1):
        if skill[s] in tree:
            idx = tree.index(skill[s])
            tree = tree[:idx]
            flag = True
        else:
            if flag:
                return False
    return True

        