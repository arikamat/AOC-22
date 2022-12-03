f = open("in.txt",'r')
l = f.readlines()
# print(l)
summ = 0
for i in range(0,len(l),3):
    group = [l[i],l[i+1],l[i+2]]
    
    for j in group[0]:
        if j in group[1] and j in group[2]:
            matchChar = j
            break
    if matchChar>='a' and matchChar<='z':
        summ += ord(matchChar)-96 
    else:
        summ += ord(matchChar)-64+26
    # print(a,b, matchChar)
print(summ)