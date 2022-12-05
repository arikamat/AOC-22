f = open("in.txt",'r')
# f = open("sample.txt",'r')
l = f.readlines()
stackCt = len(l[0])//4
c = 0
stacks=[]
for i in range(stackCt):
    stacks.append([])
for ct, i in enumerate(l):
    c = ct
    if(i[1]=='1'):
        break
    for j in range(1,len(i),4):
        if i[j] != ' ':
            stacks[((j+3)//4)-1].append(i[j])
for i in range(len(stacks)):
    stacks[i].reverse()
for i in range(ct+2,len(l),1):
    line = l[i]
    moveIdx = line.index('move ')
    fromIdx = line.index(' from')
    toIdx = line.index(' to ')
    qt = int(line[moveIdx+5:fromIdx])
    fr = int(line[fromIdx+6:toIdx])
    to = int(line[toIdx+4:].replace("\n,",""))
    print(qt,fr,to)
    for i in range(qt):
        stacks[to-1].append(stacks[fr-1].pop())

ans = ""
for i in stacks:
    ans+=i.pop()
print(stacks,ct,ans)