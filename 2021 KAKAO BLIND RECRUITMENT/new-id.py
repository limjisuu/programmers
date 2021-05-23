def solution(new_id):
    answer = ''
    acceptable = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_", "."]

    answer = new_id.lower()
    for char in answer:
        if char not in acceptable:
            answer = answer.replace(char, "")

    stack = []
    for char in answer:
        if char == ".":
            if stack and stack[-1] != ".":
                stack.append(char)
        else:
            stack.append(char)
    answer = "".join(stack)

    if answer:
        if answer[0] == ".":
            answer = answer[1:]
        if answer[-1] == ".":
            answer = answer[:-1]
    else:
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    elif len(answer) <= 2:
        answer += (answer[-1] * (3 - len(answer)))

    return answer
