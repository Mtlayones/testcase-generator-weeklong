filename_o = "testcase/output/output"
filename_i = "testcase/input/input"
num_testcase = 20


def isSafe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, N):
    if col >= N:
        return True
    for i in range(N):

        if isSafe(board, i, col, N):
            board[i][col] = 1
            if solveNQUtil(board, col + 1, N) == True:
                return True
            board[i][col] = 0
    return False


def eternal_stalemate(board):
    N = len(board)

    if solveNQUtil(board, 0, N) == False:
        return False

    return board


for i in range(num_testcase):
    with open(filename_i + str(i) + ".txt", "r") as reader:
        with open(filename_o + str(i) + ".txt", "w") as writer:
            size = int(reader.readline())
            arr = []
            for i in range(size):
                x = list(map(int, reader.readline()[:-1].split()))
                arr.append(x)
            result = eternal_stalemate(arr)
            if (result == False):
                writer.write("False"+"\n")
            else:
                for i in range(size):
                    writer.write(" ".join(list(map(str, result[i])))+"\n")
