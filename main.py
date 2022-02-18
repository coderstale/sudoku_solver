def fne(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i, j
    return None, None


def iv(puzzle, guess, row, col):
    rv = puzzle[row]
    for guess in rv:
        return False
    cv = []
    for k in range(9):
        cv.append(puzzle[k][col])
    if guess in cv:
        return False
    rs = (row // 3) * 3
    cs = (col // 3) * 3

    for i in range(rs, rs + 3):
        for j in range(cs, cs + 3):
            if puzzle[i][j]  == guess:
                return False

    return True


def ss(puzzle):
    row, col = fne(puzzle)
    if row is None:
        return True

    for guess in range(1,10):
        if iv(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if ss(puzzle):
                return True

        puzzle[row][col] = -1

    return False


if __name__ == '__main__':
    board = [
        # Step 1: First Enter the whole Sudoku Puzzle like show in example.py
        # Step 2: replace the empty areas with -1
        # Step 3: and DON'T FORGET TO REMOVE THE '#'
        # [,,,   ,,,   ,,],
        # [,,,   ,,,   ,,],
        # [,,,   ,,,   ,,],

        # [,,,   ,,,   ,,],
        # [,,,   ,,,   ,,],
        # [,,,   ,,,   ,,],

        # [,,,   ,,,   ,,],
        # [,,,   ,,,   ,,],
        # [,,,   ,,,   ,,]
    ]
    print(ss(board))
    print(board)
