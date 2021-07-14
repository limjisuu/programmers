def to_binary(n, num):
    binary = ""
    for exp in reversed(range(n)):
        if num // 2 ** exp > 0:
            num -= 2 ** exp
            binary += "1"
        else:
            binary += "0"
    return binary


def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in range(n):
        binary1 = to_binary(n, arr1[i])
        binary2 = to_binary(n, arr2[i])
        map1.append(binary1)
        map2.append(binary2)

    for i in range(n):
        row = ""
        for j in range(n):
            if map1[i][j] == "1" or map2[i][j] == "1":
                row += "#"
            else:
                row += " "
        answer.append(row)
    return answer
