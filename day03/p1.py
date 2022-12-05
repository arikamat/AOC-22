f = open("in.txt",'r')
l = f.readlines()
# print(l)
summ = 0
for i in l:
    a = i[0:len(i)//2]
    b = i[len(i)//2:len(i)]
    matchChar = ''
    for j in a:
        if j in b:
            matchChar = j
            break
    if matchChar>='a' and matchChar<='z':
        summ += ord(matchChar)-96 
    else:
        summ += ord(matchChar)-64+26
    # print(a,b, matchChar)
print(summ)