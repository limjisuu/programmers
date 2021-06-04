from itertools import permutations
import re


def calculate(expression):
    num1 = int(expression[0])
    num2 = int(expression[2])
    operator = expression[1]
    if operator == "+":
        return str(num1 + num2)
    elif operator == "-":
        return str(num1 - num2)
    elif operator == "*":
        return str(num1 * num2)


def solution(expression):
    answer = 0
    operators = ["+", "-", "*"]
    priorities = list(permutations(operators, 3))
    for priority in priorities:
        exp = re.split('([-+*])', expression)
        stack = []
        idx = 0
        while len(exp) > 1:
            for i in range(len(exp)):
                stack.append(exp[i])
                if exp[i - 1] == priority[idx]:
                    cal = calculate(stack[-3:])
                    del stack[-3:]
                    stack.append(cal)
            idx += 1
            exp = stack
            stack = []
        val = int("".join(exp))
        if abs(val) > answer:
            answer = abs(val)
    return answer
