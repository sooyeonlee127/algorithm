def solution(participant, completion):
    participant_dict = dict()
    completion_dict = dict()
    for part in participant:
        if part in participant_dict:
            participant_dict[part] += 1
        else:
            participant_dict[part] = 1
    for comp in completion:
        if comp in completion_dict:
            completion_dict[comp] += 1
        else:
            completion_dict[comp] = 1
    for part in participant:
        if part not in completion_dict:
            return part
        else:
            if completion_dict[part] < participant_dict[part]:
                return part
