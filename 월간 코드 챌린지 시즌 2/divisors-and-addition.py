def divisor(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt


def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        divisor_cnt = divisor(num)
        if divisor_cnt % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer
