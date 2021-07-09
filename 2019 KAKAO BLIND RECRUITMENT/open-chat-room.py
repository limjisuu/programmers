def solution(record):
    answer = []
    info = {}
    for message in record:
        action = message.split()[0]
        if action == "Enter" or action == "Change":
            action, user_id, name = message.split()
            info[user_id] = name

    for message in record:
        action = message.split()[0]
        user_id = message.split()[1]
        if action == "Enter":
            answer.append(info[user_id] + "님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(info[user_id] + "님이 나갔습니다.")
    return answer
