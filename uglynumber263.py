def isUgly(n):
	if n <= 0:
		return False
	while n%2==0:
		n//=2
	print("1---->",n)
	while n%3==0:
		n//=3
	print("2---->",n)
	while n%5==0:
		n//=5
	print("3---->",n)
	return n==1
	#f "shruti here n is {n}"
print(isUgly(6))
