from pprint import pprint
def neighbors(head, tail):
	same = head[0] == tail[0] and head[1] == tail[1]
	adjacent = (abs(head[0] - tail[0]) ==1 and head[1] == tail[1]) or (abs(head[1] - tail[1]) ==1 and head[0] == tail[0])
	diag = (head[0]-tail[0] == head[1]-tail[1] and abs(head[0]-tail[0]) ==1) or (head[0]-tail[0] == tail[1]-head[1] and abs(head[0]-tail[0])==1)
	return same or adjacent or diag
def adjustTail(head, tail):
	if not neighbors(head, tail):
		if head[0] == tail[0]:
			if head[1] > tail[1]:
				tail[1] += 1
			else:
				tail[1] -= 1
		elif head[1] == tail[1]:
			if head[0] > tail[0]:
				tail[0] += 1
			else:
				tail[0] -= 1
		else:
			if head[0] > tail[0]:
				tail[0] += 1
			else:
				tail[0] -= 1
			if head[1] > tail[1]:
				tail[1] += 1
			else:
				tail[1] -= 1
		
	return tail

# f = open('sample.txt','r')
# f = open('sample2.txt','r')

f = open('in.txt','r')
lines = f.readlines()

width = 2000
height = 2000

grid = [[0 for x in range(width)] for y in range(height)]
numberKnots = 10
coord = 1000
knots = [[coord,coord] for x in range(numberKnots)]


# for i in range(numberKnots):
# 	knots.append([coord,coord])

grid[coord][coord]=1
for i in lines:
	dir = i.split(' ')[0]
	steps = int(i.split(' ')[1])
	head = knots[0]
	tail = knots[-1]

	if dir == 'R':
		for j in range(steps):
			head[0] += 1
			for i in range(1,numberKnots,1):
				knots[i] = adjustTail(knots[i-1], knots[i])
				tail = knots[-1]
			grid[tail[1]][tail[0]]=1

	elif dir == 'L':
		for j in range(steps):
			head[0] -= 1
			for i in range(1,numberKnots,1):
				knots[i] = adjustTail(knots[i-1], knots[i])
				tail = knots[-1]
			grid[tail[1]][tail[0]]=1

	elif dir == 'U':
		for j in range(steps):
			head[1] += 1
			for i in range(1,numberKnots,1):
				knots[i] = adjustTail(knots[i-1], knots[i])
				tail = knots[-1]
			grid[tail[1]][tail[0]]=1


	elif dir == 'D':
		for j in range(steps):
			head[1] -= 1
			for i in range(1,numberKnots,1):
				knots[i] = adjustTail(knots[i-1], knots[i])
				tail = knots[-1]
			grid[tail[1]][tail[0]]=1
	
ct=0
for i in grid:
	for j in i:
		if j == 1:
			ct +=1
# pprint(grid)
print(ct)
