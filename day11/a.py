f = open('in.txt','r')

lines = f.readlines()
class Monkey:
	def __init__(self, starting_items, operation, test, trueCond, falseCond):
		self.starting_items = starting_items
		self.operation = operation
		self.test = test
		self.trueCond = trueCond
		self.falseCond = falseCond
class Operation:
	def __init__(self, operation, withVal):
		self.operation = operation
		self.withVal = withVal
monkeys = []

for i in range(0,len(lines),7):
	l = lines[i+1]
	a = l.index(':')
	starting_items = l[a+2:].split(',')
	starting_items = [int(x) for x in starting_items]
	
	l = lines[i+2]
	a = l.index('=')
	arr = l[a+2:].split(' ')
	operation = Operation(arr[1],arr[2].strip())

	l = lines[i+3]
	a = l.index('by')
	divisible = int(l[a+3:].strip())
	
	l = lines[i+4]
	a = l.index('monkey')
	trueCond = int(l[a+7:].strip())

	l = lines[i+5]
	a = l.index('monkey')
	falseCond = int(l[a+7:].strip())

	monkeys.append(Monkey(starting_items,operation,divisible,trueCond,falseCond))
	# print(trueCond,falseCond)
# print("length", len(monkeys))
c =0
monkeyChecks=[0]*len(monkeys)
for i in range(len(monkeys)*20):
	print(i)
	m = monkeys[i%len(monkeys)]
	while len(m.starting_items) >0:
		# print(m.starting_items)
		item = m.starting_items[0]
		m.starting_items.pop(0)
		monkeyChecks[i%len(monkeys)] += 1
		oper = m.operation.operation
		withVal = m.operation.withVal
		if oper == '+':
			if(withVal.lower()=='old'):
				item += item
			else:
				item += int(withVal)
		elif oper == '*':
			if(withVal.lower()=='old'):
				item *= item
			else:
				item *= int(withVal)
		elif oper == '-':
			if(withVal.lower()=='old'):
				item -= item
			else:
				item -= int(withVal)
		elif oper == '/':
			if(withVal.lower()=='old'):
				item = item//item
			else:
				item = item// int(withVal)

		item = item//3

		if item % m.test == 0:
			monkeys[m.trueCond].starting_items.append(item)
		else:
			# import pdb
			# pdb.set_trace()
			monkeys[m.falseCond].starting_items.append(item)
	
	if(i%len(monkeys)==len(monkeys)-1):
		print('#'*30)
		for i in monkeys:
			print(i.starting_items)
		print('#'*30)
max1 = max(monkeyChecks)
monkeyChecks.remove(max1)
max2 = max(monkeyChecks)
print(max1,max2,max1*max2)