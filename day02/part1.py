f = open("in.txt",'r')

l = f.readlines()
ans=[]
for i in l:
    aa = i.split()
    a = aa[0]
    b = aa[1]
    win = False
    
    if a== 'A':
        win = b=='Y'
    elif a=='B':
        win = b=='Z'
    else:
        win = b=='X'
    
    score = 0
    if win:
        score+=6
    elif a=='A' and b=='X' or a=='B' and b=='Y' or a=='C' and b=='Z':
        score+=3
    else:
        score+=0
    
    if(b == 'X'):
        score+=1
    elif(b == 'Y'):
        score+=2
    else:
        score+=3    
    ans.append(score)

print(sum(ans))
