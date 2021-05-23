def solution(lottos, win_nums):
    answer = []
    win_cnt = 0
    zero_cnt = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            win_cnt += 1
    highest_rank = 7 - (win_cnt + zero_cnt)
    lowest_rank = 7 - win_cnt
    if highest_rank > 6:
        highest_rank = 6
    if lowest_rank > 6:
        lowest_rank = 6
    answer.append(highest_rank)
    answer.append(lowest_rank)
    return answer
