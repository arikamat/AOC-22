f = open("in.txt",'r')
# f = open("sample.txt",'r')
l = f.readlines()
ct = 0
for i in l:
    a = i.replace("\n","").split(',')
    firstPairA = int(a[0].split('-')[0])
    firstPairB = int(a[0].split('-')[1])

    secondPairA = int(a[1].split('-')[0])
    secondPairB = int(a[1].split('-')[1])
    
    setA = set(range(firstPairA,firstPairB+1))
    setB = set(range(secondPairA,secondPairB+1))
    # 2 6
    # 3 5

    if(not setA.isdisjoint(setB)):
        ct+=1
        print(firstPairA,firstPairB,secondPairA,secondPairB)
    
print(ct)