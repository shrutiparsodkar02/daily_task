import random

def display(grid):
    """Display the Sudoku grid."""
    print("\nSudoku Grid:")
    for row in grid:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))
    print()

def generate_sudoku(size):
    """Generate a partially filled Sudoku grid."""
    grid = [[0] * size for _ in range(size)]
    # Fill the diagonal subgrids to make a valid base grid
    subgrid_size = int(size ** 0.5)
    for i in range(0, size, subgrid_size):
        fill_subgrid(grid, i, i, size)
    # Randomly remove some numbers to create a puzzle
    remove_numbers(grid, size)
    return grid

def fill_subgrid(grid, start_row, start_col, size):
    """Fill a subgrid with unique numbers."""
    nums = list(range(1, size + 1))
    random.shuffle(nums)
    subgrid_size = int(size ** 0.5)
    for i in range(subgrid_size):
        for j in range(subgrid_size):
            grid[start_row + i][start_col + j] = nums.pop()

def remove_numbers(grid, size):
    """Remove some numbers from the grid to create the puzzle."""
    total_cells = size * size
    cells_to_remove = total_cells // 2  # Remove half the cells
    for _ in range(cells_to_remove):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[row][col] = 0

def is_valid_move(grid, row, col, num, size):
    """Check if placing 'num' at grid[row][col] is valid."""
    # Check row and column
    if num in grid[row] or num in [grid[r][col] for r in range(size)]:
        return False
    # Check subgrid
    subgrid_size = int(size ** 0.5)
    start_row, start_col = (row // subgrid_size) * subgrid_size, (col // subgrid_size) * subgrid_size
    for i in range(subgrid_size):
        for j in range(subgrid_size):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def play_sudoku(grid, size):
    """Let the user play Sudoku."""
    while True:
        display(grid)
        try:
            row = int(input("Enter row (1-based, 0 to quit): ")) - 1
            if row == -1:
                print("Exiting game.")
                break
            col = int(input("Enter column (1-based): ")) - 1
            num = int(input("Enter number: "))
            if grid[row][col] != 0:
                print("Cell is already filled. Try again.")
            elif is_valid_move(grid, row, col, num, size):
                grid[row][col] = num
                if all(0 not in row for row in grid):
                    print("Congratulations! You solved the Sudoku!")
                    display(grid)
                    break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def sudoku():
    """Main function to run Sudoku."""
    size = 9  # Standard Sudoku grid size
    grid = generate_sudoku(size)
    play_sudoku(grid, size)

sudoku()

