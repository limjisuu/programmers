from itertools import combinations


def solution(orders, course):
    answer = []
    for n in course:
        dic = {}
        for order in orders:
            single_menus = list(map(str, order))
            course_menus = list(combinations(single_menus, n))
            for menu in course_menus:
                menu = sorted(list(menu))
                menu_name = "".join(menu)
                if menu_name in dic.keys():
                    dic[menu_name] += 1
                else:
                    dic[menu_name] = 1
        for item in dic.items():
            max_val = max(dic.values())
            if item[1] == max_val and max_val >= 2:
                answer.append(item[0])
    answer.sort()
    return answer
