def incrementC(c,reg, vals):
	c+=1
	if (c-20) >=0 and (c-20)%40==0:
		vals.append(reg)
	return c
f = open('sample.txt','r')
f = open('in.txt','r')

lines = f.readlines()
ct = 0
reg = 1
vals=[]
for i in lines:
	a = i.split(' ')
	if len(a) == 1:
		ct = incrementC(ct, reg,vals)
	else:
		for i in range(2):
			ct = incrementC(ct,reg,vals)
		reg+=int(a[1])
ans=0
for c,i in enumerate(vals):
	a = 20+40*(c)
	print(a)
	if a <=220:
		ans += a*i
print(ans)	