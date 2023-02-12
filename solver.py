# Loops through the matrix and checks for any 0's (missing numbers)
def check_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                return i, j


# Function that solves the sudoku puzzle
def solve(matrix):
    # Checks if there are any 0's in matrix
    # If there are no 0's in the matrix, we finish (base case)
    test = check_zero(matrix)
    if not test:
        return True
    else:
        x, y = test
    # Loops through every possible input in sudoku
    for z in range(1, 10):
        if check(z, x, y, matrix):
            matrix[x][y] = z
            # After adding the new value, we will continue to solve from that point forwards with the new value
            if solve(matrix):
                return True
            # If there are no solutions beyond this point, we reset the value and "backtrack"
            matrix[x][y] = 0
    return False


# Checks if the number satisfies the rules of sudoku
def check(num, row, col, matrix):
    # Checks if there is duplicate number in same row
    for i in range(len(matrix)):
        if matrix[row][i] == num:
            return False
    # Checks if there is duplicate number in same column
    for i in range(len(matrix)):
        if matrix[i][col] == num:
            return False
    # Checks if there is a  duplicate number in same 3x3 subarray
    start_x = row // 3 * 3
    start_y = col // 3 * 3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if matrix[i][j] == num:
                return False
    # If all rules are satisfied, function returns true
    return True
