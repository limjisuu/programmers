def is_right(u):
    stack = []
    for bracket in u:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if stack:
                stack.pop()
            else:
                return False
    return True


def to_balanced(w):
    for i in range(1, len(w)):
        string = w[:i + 1]
        if string.count("(") == string.count(")"):
            u, v = w[:i + 1], w[i + 1:]
            break
    return [u, v]


def solution(p):
    answer = ''
    if p:
        u, v = to_balanced(p)
        if is_right(u):
            answer = u + solution(v)
        else:
            answer += "(" + solution(v) + ")"
            for bracket in u[1:-1]:
                if bracket == "(":
                    answer += ")"
                elif bracket == ")":
                    answer += "("
    return answer
