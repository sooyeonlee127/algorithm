

answer = []

def solution(user_id, banned_id):
    global answer
    check = dict()
    for i in user_id:
        check[i] = 0
    
    result = check_same_id(user_id, banned_id)
    dfs(0, check, result)
    return len(answer)

def dfs(level, used, checked_id):
    global answer, answer_list
    if level == len(checked_id):
        lst = []
        for i in used:
            if used[i] == 1:
                lst.append(i)
        if lst not in answer:
            answer.append(lst)
        return
    
    for i in range(len(checked_id[level])):
        if used[checked_id[level][i]] == 1: continue
        used[checked_id[level][i]] = 1
        dfs(level+1, used, checked_id)
        used[checked_id[level][i]] = 0


def check_same_id(user_id, banned_id):
    lst = []
    for i in range(len(banned_id)):
        lst.append([])
        for j in range(len(user_id)):
            if len(banned_id[i]) != len(user_id[j]): continue
            flag = True
            for k in range(len(banned_id[i])):
                if banned_id[i][k] == '*': continue
                if banned_id[i][k] != user_id[j][k]:
                    flag = False
                    break
            if flag:
                lst[i].append(user_id[j])
    return lst
    