class Directory:
	def __init__(self, name, parent, dir, size=0):
		self.name = name
		self.parent = parent
		self.dir = dir
		# if parent is not None:
		# self.parent.add_child(self)
		self.children = []
		self.size = size

	def add_child(self, child):
		self.children.append(child)

	def set_size(self, size):
		self.size = size


def get_size(dir):
	if dir.size != 0:
		return dir.size
	else:
		size = 0
		for child in dir.children:
			size += get_size(child)
		dir.set_size(size)
		return size


def find_small_dirs(dir, needToRemove, possible_dirs):
	# print("aa",dir.name, dir.size)
	if dir.size >= needToRemove:
		possible_dirs.append(dir)
	for i in dir.children:
		if i.dir:
			find_small_dirs(i, needToRemove, possible_dirs)


# f = open("sample.txt",'r')
f = open("in.txt", "r")
totalAvailable = 70000000
needed = 30000000
lines = f.readlines()
i = -1

root = Directory("root", None, True)
current = root
for c in range(len(lines)):
	i = lines[c]
	if i[0:4] == "$ cd":
		p = i[4:].strip()
		if p == "..":
			current = current.parent
		elif p == "/":
			current = root
		else:
			new_dir = Directory(p, current, True)
			current.add_child(new_dir)
			current = new_dir
	elif i[0:4] == "$ ls":
		c += 1
		i = lines[c]
		while i[0] != "$":
			if c >= len(lines):
				break
			i = lines[c]

			# print(size, file_dir)
			if i[0] != "$":
				size = i.split(" ")[0]
				file_dir = i.split(" ")[1].strip()

				if size.isdigit():
					aa = True
					for child in current.children:
						if child.name == file_dir:
							aa = False
					if aa:
						# print(current.name, file_dir)
						new_dir = Directory(file_dir, current, False)
						new_dir.set_size(int(size))
						current.add_child(new_dir)
			c += 1

get_size(root)

totalSize = root.size
unusedSize = 70000000 - totalSize
needToRemove = 30000000 - unusedSize

minn = float("inf")
minDir = root

possible_dirs = []

find_small_dirs(root, needToRemove, possible_dirs)
# print(answer)
for i in possible_dirs:
	if i.size < minn:
		minn = i.size
		minDir = i
print(minn, minDir.name)
# # print('#'*50)
# finalAnswerSum=0
# for i in answer:
#     # print(i.name)
#     finalAnswerSum+=i.size
# print(finalAnswerSum)
# # import pdb
# pdb.set_trace()
