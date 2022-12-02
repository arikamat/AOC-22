f = open("in.txt", "r")
lines = f.readlines()
a=[0]*1000
i = 0
for j in lines:
    if(j!="\n"):
        a[i] += int(j.replace("\n",""))
    else:
        i+=1

a1 = max(a)
a.remove(a1)

a2 = max(a)
a.remove(a2)

a3 = max(a)
a.remove(a3)

print(a1+a2+a3)