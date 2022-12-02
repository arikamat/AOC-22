f = open("in.txt",'r')

l = f.readlines()
ans=[]
for i in l:
    score = 0
    aa = i.split()
    a = aa[0]
    c = aa[1]
    win = False
    b=''
    if c=='X':
        # needs to lose
        if a=='A':
            b = 'Z'
        elif a=='B':
            b = 'X'
        else:
            b = 'Y'
        score += 0
    elif c=='Y':
        # needs to draw
        if a=='A':
            b = 'X'
        elif a=='B':
            b = 'Y'
        else:
            b = 'Z'
        score+=3
    else:
        # needs to win
        if a=='A':
            b = 'Y'
        elif a=='B':
            b = 'Z'
        else:
            b = 'X'
        score += 6
    
    
    # if win:
    #     score+=6
    # elif a=='A' and b=='X' or a=='B' and b=='Y' or a=='C' and b=='Z':
    #     score+=3
    # else:
    #     score+=0
    
    if(b == 'X'):
        score+=1
    elif(b == 'Y'):
        score+=2
    else:
        score+=3    
    #print(b)
    ans.append(score)

#print(ans)
print(sum(ans))
