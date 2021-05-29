def solution(dartResult):
    answer = 0
    stack = []
    for string in dartResult:
        if string in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if stack and stack[-1] == 1 and string == "0":
                stack.pop()
                stack.append(10)
            else:
                stack.append(int(string))
        elif string == "D":
            stack[-1] **= 2
        elif string == "T":
            stack[-1] **= 3
        elif string == "*":
            if len(stack) == 1:
                stack[-1] *= 2
            else:
                stack[-1] *= 2
                stack[-2] *= 2
        elif string == "#":
            stack[-1] *= -1
    answer = sum(stack)
    return answer
