def solution(str1, str2):
    answer = 0
    str1_set = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2_set = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    temp = str1_set.copy()
    intersection = []
    for val in str2_set:
        if val in temp:
            intersection.append(val)
            temp.remove(val)

    temp = intersection.copy()
    str2_subset = []
    for val in str2_set:
        if val not in temp:
            str2_subset.append(val)
        else:
            temp.remove(val)
    union = str1_set + str2_subset

    if not intersection and not union:
        answer = 65536
    else:
        answer = int(len(intersection) / len(union) * 65536)
    return answer
