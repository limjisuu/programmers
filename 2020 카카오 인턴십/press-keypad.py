def solution(numbers, hand):
    answer = ''
    locations = {
        1: [0, 0],
        2: [1, 0],
        3: [2, 0],
        4: [0, 1],
        5: [1, 1],
        6: [2, 1],
        7: [0, 2],
        8: [1, 2],
        9: [2, 2],
        "*": [0, 3],
        0: [1, 3],
        "#": [2, 3]
    }

    x = 0
    y = 1
    left = "*"
    right = "#"
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            left_distance = abs(locations[left][x] - locations[num][x]) + abs(locations[left][y] - locations[num][y])
            right_distance = abs(locations[right][x] - locations[num][x]) + abs(locations[right][y] - locations[num][y])
            if left_distance > right_distance:
                right = num
                answer += 'R'
            elif left_distance < right_distance:
                left = num
                answer += "L"
            else:
                if hand == "left":
                    left = num
                    answer += "L"
                elif hand == "right":
                    right = num
                    answer += "R"

    return answer
