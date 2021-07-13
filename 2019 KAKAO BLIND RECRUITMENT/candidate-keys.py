from itertools import combinations


def is_unique(candidate):
    if len(candidate) == len(set(candidate)):
        return True
    return False


def solution(relation):
    answer = 0
    row = len(relation)
    column = len(relation[0])

    combination_list = []
    for i in range(1, column + 1):
        combination_list.extend(combinations(range(column), i))

    candidate_keys = []
    for combination in combination_list:
        temp = [tuple(record[col] for col in combination) for record in relation]
        if is_unique(temp):
            candidate_keys.append(combination)

    result = set(candidate_keys)
    for i in range(len(candidate_keys)):
        set1 = set(candidate_keys[i])
        for j in range(i + 1, len(candidate_keys)):
            set2 = set(candidate_keys[j])
            if set1.intersection(set2) == set1:
                result.discard(candidate_keys[j])
    answer += len(result)
    return answer
