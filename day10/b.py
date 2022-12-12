from pprint import pprint
def incrementC(c,reg, vals):
	c+=1
	# print("c",c)
	row = (c-1)//40
	col = (c-1)%40
	
	colS = (reg-1)%40
	print("c",c, "reg", reg, "row",row,"col",col, "colS",colS)
	print(''.join(vals[row]))
	print("\n")
	if abs(col-1-colS)<2:
		# print("row",row)
		vals[row][col] = '#'
	else:
		vals[row][col] = '.'
	# print(reg)
	return c
# f = open('sample.txt','r')
f = open('in.txt','r')

lines = f.readlines()
ct = 0
reg = 1
vals=[]
for i in range(6):
	vals.append([' ']*40)
for i in lines:
	a = i.split(' ')
	if len(a) == 1:
		ct = incrementC(ct, reg,vals)
		# print(ct,reg)

	else:
		for i in range(2):
			ct = incrementC(ct,reg,vals)
			# print(ct,reg)
		reg+=int(a[1])
	# print(reg)
	# print(vals)
	# break
ans=0
# for c,i in enumerate(vals):
# 	a = 20+40*(c)
# 	print(a)
# 	if a <=220:
# 		ans += a*ipri
print()
print('#'*40)
print(	)
for i in vals:
	print(''.join(i))
print(ans)