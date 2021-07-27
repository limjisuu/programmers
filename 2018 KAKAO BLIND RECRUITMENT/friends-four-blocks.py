def pop_blocks(m, n, board):
    removed = []
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i][j+1] and board[i][j] != "*":
                if board[i+1][j] == board[i+1][j+1] == board[i][j]:
                    removed += [(i, j), (i, j+1), (i+1, j), (i+1, j+1)]
    removed = set(removed)
    return removed


def relocate_blocks(m, n, board, removed):
    for i in range(m):
        board[i] = list(board[i])
        for j in range(n):
            if (i, j) in removed:
                board[i][j] = "*"
    temp = [[] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            temp[j].append(board[i][j])
    for i in range(m):
        cnt = temp[i].count("*")
        temp[i] = [item for item in temp[i] if item != "*"]
        temp[i] = ["*"] * cnt + temp[i]

    for i in range(m):
        for j in range(n):
            board[i][j] = temp[j][i]
    return board


def solution(m, n, board):
    answer = 0
    while 1:
        removed = pop_blocks(m, n, board)
        if not removed:
            break
        answer += len(removed)
        board = relocate_blocks(m, n, board, removed)
    return answer
