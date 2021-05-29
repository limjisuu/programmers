def solution(s):
    answer = []
    number = ""
    dic = {}
    for char in s:
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            number += char
        else:
            if number:
                if int(number) not in dic.keys():
                    dic[int(number)] = 1
                else:
                    dic[int(number)] += 1
                number = ""
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for element in sorted_dic:
        answer.append(element[0])
    return answer
