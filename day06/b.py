f = open("in.txt",'r')
# f = open("sample.txt",'r')
l = f.readline()
for i in range(0,len(l)-14,1):
    if len(set(l[i:i+14]))==14:
        print(i+14)
        break
