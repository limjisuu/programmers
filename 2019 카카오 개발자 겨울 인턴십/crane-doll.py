def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                removed = row[move - 1]
                row[move - 1] = 0
                if basket and removed == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(removed)
                break
    return answer
