def solution(N, stages):
    answer = []
    dict = {}
    for i in range(1, N + 1):
        challengers = 0
        failures = 0
        for stage in stages:
            if stage >= i:
                challengers += 1
            if stage == i:
                failures += 1
        if failures == 0:
            dict[i] = 0
        else:
            dict[i] = failures / challengers
    new_dict = dict.items()
    sorted_stages = sorted(new_dict, key=lambda x:x[1], reverse=True)
    for stage in sorted_stages:
        answer.append(stage[0])
    return answer
