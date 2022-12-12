f = open("in.txt",'r')
# f = open("sample.txt",'r')
l = f.readline()
for i in range(0,len(l)-4,1):
    if len(set(l[i:i+4]))==4:
        print(i+4)
        break
