import random
def is_attacking(q1,q2):
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q2[1] - q1[1]) == abs(q2[0] - q1[0]):
        return False
    else:
        return True


def check_queens(queens):
    for i in range(0, len(queens)-1):
        for j in range(i+1,len(queens)) :
            if  is_attacking(queens[i], queens[j]):
                pass
            else:
                return False
    return True

def generate_boards():
    board_list = []
    while len(board_list) < 4:
        queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
        if check_queens(queens):
            board_list.append(queens)
    return board_list

print(generate_boards())