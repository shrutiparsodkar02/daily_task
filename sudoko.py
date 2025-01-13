import random
def generate_sudoku(size):#initial method,,
	sudoku_grid = {(row, col):" " for row in range(size) for col in range(size)}
	return sudoku_grid
def fill_grid(size):
	sudoku_grid = {(row, col):" " for row in range(size) for col in range(size)}
	p=set(range(1,size+1))
	for r in range(size):
		for c in range(size):
			a=set(sudoku_grid[r]+row[c] for row in sudoku_grid)
			cand=list(p-a)
			if cand:
				sudoku_grid=cand[random.randint(0,len(cand)-1)]
			else:
				return fill_grid(size)
			'''n=random.randint(1,size)
			while (n in [sudoku_grid[(i, col)] for col in range(size)] or n in [sudoku_grid[(row, j)] for row in range(size)]):
				n=random.randint(1,size)
			sudoku_grid[(i,j)]=n'''
	return sudoku_grid
def display_grid(grid,size):
	hr_l="--"*size
	print(hr_l)
	fs="{}|"*size
	fs="|"+fs
	
	for r in range(size):
		row_values = [grid[(r, c)] for c in range(size)]
		print(fs.format(*row_values))
	print(hr_l)
'''def print_grid(grid,size):
	for i in range(1,size+1):
		row="|".join(grid[i,y] for y in range(1,size+1))
		print(row)
		if i !=size:
			print("-"*(2*size))
def is_valid(num, row, col):
	for i in range(9):
		if sudoku_grid[(row, i)] == num:
			return False
	for i in range(9):
		if sudoku_grid[(i, col)] == num:
			return False
	start_row, start_col = 3 * (row // 3), 3 * (col // 3)
	for i in range(start_row, start_row + 3):
		for j in range(start_col, start_col + 3):
			if sudoku_grid[(i, j)] == num:
				return False
	return True'''
size=3
#g=generate_sudoku(size)
g=fill_grid(size)

#print_grid(g,size)
display_grid(g,size)
