from pprint import pprint
def checkFromTop(grid, row, col):
	ct=0
	val = grid[row][col]
	for i in range(row-1,-1,-1):
		ct+=1
		if grid[i][col] >= val:
			return ct
	return ct

def checkFromBottom(grid, row, col):
	ct=0
	val = grid[row][col]
	for i in range(row+1,len(grid),1):
		ct+=1
		if grid[i][col] >= val:
			return ct
	return ct

def checkFromLeft(grid, row, col):
	ct=0
	val = grid[row][col]
	for i in range(col-1,-1,-1):
		ct+=1
		# print('a',grid[row][i])
		if grid[row][i] >= val:
			return ct
	return ct

def checkFromRight(grid, row, col):
	ct=0
	val = grid[row][col]
	for i in range(col+1,len(grid[row]),1):
		ct+=1
		if grid[row][i] >= val:
			return ct
	return ct

def main(f):
	lines = f.readlines()
	height = len(lines)
	width = len(lines[0].strip())
	grid = [[0 for x in range(width)] for y in range(height)]

	for row,i in enumerate(lines):
		for col,j in enumerate(i.strip()):
			grid[row][col] = j
	# pprint(grid)
	max = -1
	ct=0
	for row in range(1, len(grid)-1,1):
		for col in range(1, len(grid[row])-1,1):
			a= checkFromTop(grid, row, col)
			b= checkFromLeft(grid, row, col)
			c= checkFromRight(grid, row, col)
			d= checkFromBottom(grid, row, col)
			# print(grid[row][col],a,b,c,d)
			if a*b*c*d >max:
				max = a*b*c*d
	# a = checkFromLeft(grid,1,2)
	# print(grid[1][2],a)
	print(max)
				

if __name__ == '__main__':
	f = open('in.txt', 'r')
	# f = open('sample.txt','r')
	main(f)