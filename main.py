# Program that solves Sudoku Puzzle based on user inputted numbers


# Function to check user inputs and make sure they are correct
def getRow(prompt):
    isTrue = True
    response = input(prompt)
    while isTrue:
        try:
            response_ = list(map(int, response.split()))
            if len(response_) > 9 or len(response_) < 9:
                print("Your row is greater or less than 9 numbers.  Please make sure your row contains exactly 9 numbers")

            else:
                return response_
            response = input()
        except ValueError:
            print("Please enter only numbers.")
            response = input()


row_1 = getRow("Place Numbers on Sudoku board sequentially left to right (starting at top left)\nPlace the number"
               "'0' in for blank spaces.  \nSEPERATE EACH NUMBER BY A SPACE\nPlease enter first row\n:")
row_2 = getRow("Please input second row\n:")
row_3 = getRow("Please input third row\n:")
row_4 = getRow("Please input fourth row\n:")
row_5 = getRow("Please input fifth row\n:")
row_6 = getRow("Please input sixth row\n:")
row_7 = getRow("Please input seventh row\n:")
row_8 = getRow("Please input eighth row\n:")
row_9 = getRow("Please input Final row\n:")

board = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]


# Finds empty square
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col

    return None


def solveBoard(bo):
    # check if board solved if find empty returned none
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    # checking num 1-9 for valid number
    for i in range(1, 10):
        if isValid(bo, i, (row, col)):
            bo[row][col] = i
            # call solve Board to get next number
            if solveBoard(bo):
                return True
            # if SolveBoard is False reset last value
            bo[row][col] = 0

    return False


# Function used to determine if number in [row,col] is a valid number for the Sudoku Puzzle
def isValid(bo, num, pos):
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # checking row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # checking col
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # checking box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# Function used to print the Sudoku board in a readable way
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


print("UNSOLVED SUDOKU PUZZLE")
print_board(board)
solveBoard(board)
print("            ")
print("SOLVED SUDOKU PUZZLE")
print_board(board)
