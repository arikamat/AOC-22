from pprint import pprint
def checkFromTop(grid, row, col):
	val = grid[row][col]
	for i in range(0,row,1):
		if grid[i][col] >= val:
			return False
	return True

def checkFromBottom(grid, row, col):
	val = grid[row][col]
	for i in range(row+1,len(grid),1):
		if grid[i][col] >= val:
			return False
	return True

def checkFromLeft(grid, row, col):
	val = grid[row][col]
	for i in range(0,col,1):
		if grid[row][i] >= val:
			return False
	return True

def checkFromRight(grid, row, col):
	val = grid[row][col]
	for i in range(col+1,len(grid[row]),1):
		if grid[row][i] >= val:
			return False
	return True

def main(f):
	lines = f.readlines()
	height = len(lines)
	width = len(lines[0].strip())
	grid = [[0 for x in range(width)] for y in range(height)]

	for row,i in enumerate(lines):
		for col,j in enumerate(i.strip()):
			grid[row][col] = j
	pprint(grid)
	ct = 0
	for row in range(1, len(grid)-1,1):
		for col in range(1, len(grid[row])-1,1):
			a= checkFromTop(grid, row, col)
			b= checkFromBottom(grid, row, col)
			c= checkFromLeft(grid, row, col)
			d= checkFromRight(grid, row, col)
			# print(grid[row][col],a,b,c,d)
			if a or b or c or d:
				ct+=1
	print(ct+height+height+width+width-4)
				

if __name__ == '__main__':
	f = open('in.txt', 'r')
	# f = open('sample.txt','r')
	main(f)