def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    cnt_list = [0]*len(id_list)
    id_dict = dict()
    for rep in report:
        rep = list(map(str, rep.split(' ')))
        idx = id_list.index(rep[1])
        cnt_list[idx] += 1
        if rep[0] in id_dict:
            id_dict[rep[0]].append(rep[1])
        else:
            id_dict[rep[0]] = [rep[1]]
    for id in id_list:
        if id not in id_dict:
            answer.append(0)
        else:
            tmp = 0
            for i in id_dict[id]:
                idx = id_list.index(i)
                if cnt_list[idx] >= k:
                    tmp +=1
            answer.append(tmp)
    return answer