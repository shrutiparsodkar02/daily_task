'''i=0
while i>=0 | i<=10:
	print(i)
	i+=2
li=[10,20,30,40,50]
sum=0
i=0
while i<len(li):
	sum+=li[i]
	i+=1;

for i in range(0,9):
	for j in range(0,i+1):
		print("*",end="")
	print()
for i in range(9,0,-1):
	 for j in range(i,0,-1):
	 	print("*",end="")
	 print()'''
for i in range(1,11):
	for j in range(1,11):
		sum=0
		sum=i*j
		print('{:4}'.format(sum),end="  ")
	print()
