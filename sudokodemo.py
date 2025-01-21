import random

def generate_sudoku(grid_size=9, difficulty="Easy"):
    def is_valid(grid, row, col, num):
        # Check row and column
        for i in range(grid_size):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        # Check sub-grid
        sub_size = int(grid_size ** 0.5)
        start_row, start_col = row - row % sub_size, col - col % sub_size
        for i in range(start_row, start_row + sub_size):
            for j in range(start_col, start_col + sub_size):
                if grid[i][j] == num:
                    return False
        return True

    def fill_grid(grid):
        for row in range(grid_size):
            for col in range(grid_size):
                if grid[row][col] == 0:
                    for num in random.sample(range(1, grid_size + 1), grid_size):
                        if is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if fill_grid(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    # Initialize empty grid
    grid = [[0] * grid_size for _ in range(grid_size)]
    fill_grid(grid)

    # Remove cells based on difficulty
    difficulty_map = {"Easy": 0.5, "Medium": 0.7, "Hard": 0.8}
    remove_cells = int(grid_size * grid_size * difficulty_map[difficulty])
    for _ in range(remove_cells):
        x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        grid[x][y] = 0

    return grid

# Example usage
sudoku = generate_sudoku(difficulty="Medium")
for row in sudoku:
    print(row)

