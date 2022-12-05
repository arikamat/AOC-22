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
    
    # 2 6
    # 3 5

    if(firstPairA<=secondPairA and firstPairB>=secondPairB):
        ct+=1
        print(firstPairA,firstPairB,secondPairA,secondPairB)
    elif(firstPairA>=secondPairA and firstPairB<=secondPairB):
        ct+=1
        print(firstPairA,firstPairB,secondPairA,secondPairB)

    
print(ct)