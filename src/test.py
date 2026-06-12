board = dict()
for i in ["R", "G", "B", "Y"]:
    for j in range(1, 13):
        board[i+str(j)] = 0
    for j in range(1, 6):
        board[i+str(j)+"L"] = 0
    for j in range(1, 5):
        board[i+str(j)+"B"] = 0
    board[i+"W"] = 0
print(board)