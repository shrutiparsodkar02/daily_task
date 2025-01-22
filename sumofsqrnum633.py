'''def judgeSquareSum(c):
	l=list(range(1,c))
	#print(l)
	for i in range(len(l)-1):
		a=l[i]
		b=l[i+1]
		#print(a*a)
		#print(b*b)
		if (a*a+b*b)==c:
			return True
	return False
print(judgeSquareSum(5))'''
def judgeSquareSum(c):
	left,right=0,int(c**0.5)
	while left<=right:
		ans=left*left+right*right
		if ans==c:
			return True
		elif ans>c:
			right-=1
		else:
			left+=1
	return False
print(judgeSquareSum(3))
