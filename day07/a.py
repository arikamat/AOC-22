
class Directory:
	def __init__(self, name, parent, dir, size=0):
		self.name = name
		self.parent = parent
		self.dir = dir
		self.children = []
		self.size = size
	def add_child(self, child):
		self.children.append(child)
	def set_size(self, size):
		self.size = size

def calculate_nested_sizes(dir):
	if dir.size != 0:
		return dir.size
	else:
		size = 0
		for child in dir.children:
			size += calculate_nested_sizes(child)
		dir.set_size(size)
		return size


def find_small_dirs(dir, good_dirs):
	if(dir.size<100000):
		good_dirs.append(dir)
	for i in dir.children:
		if i.dir:
			find_small_dirs(i,good_dirs)
def main(f):           

	lines = f.readlines()

	root = Directory("root", None,True)

	current = root
	for c in range(len(lines)):
		i = lines[c]
		if i[0:4] == '$ cd':
			p = i[4:].strip()
			if p == '..':
				current = current.parent
			elif p == '/':
				current = root
			else:
				new_dir = Directory(p, current,True)
				current.add_child(new_dir)
				current = new_dir
		elif i[0:4] == '$ ls':
			c+=1
			i = lines[c]
			while(i[0] != '$'):
				if(c >= len(lines)):
					break
				i = lines[c]
				
				if i[0] != '$':
					size = i.split(' ')[0]
					file_dir = i.split(' ')[1].strip()

					if size.isdigit():
						duplicate = False
						for child in current.children:
							if child.name == file_dir:
								duplicate = True
								break
						if not duplicate:
							new_dir = Directory(file_dir, current,False)
							new_dir.set_size(int(size))
							current.add_child(new_dir)
				c += 1
	calculate_nested_sizes(root)

	good_dirs=[]

	find_small_dirs(root,good_dirs)

	answer=0
	for i in good_dirs:
		answer+=i.size
	print(answer)


if __name__ == "__main__":
	# f = open("sample.txt",'r')
	f = open("in.txt",'r')
	main(f)