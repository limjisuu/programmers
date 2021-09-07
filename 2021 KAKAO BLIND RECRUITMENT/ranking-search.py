from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for i in info:
        conditions = i.split()
        conditions, score = conditions[:-1], int(conditions[-1])
        for n in range(5):
            for combination in list(combinations(conditions, n)):
                combination = "".join(combination)
                dic[combination].append(score)

    for value in dic.values():
        value.sort()

    for q in query:
        conditions = q.split()
        conditions = [c for c in conditions if c != "and" and c != "-"]
        conditions, min_score = "".join(conditions[:-1]), int(conditions[-1])
        if conditions in dic.keys():
            scores = dic[conditions]
            start, end = 0, len(scores)
            while start < end:
                mid = (start + end) // 2
                if scores[mid] >= min_score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer
