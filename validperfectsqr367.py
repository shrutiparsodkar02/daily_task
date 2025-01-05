def isPerfectSquare(num):
	if num<2:
		return True # as 0 and 1 is perfect square
	left,right=2,num//2
	while(left<=right):
		mid=left+(right-left)/2
		sqr=mid*mid
		if sqr==num:
			return True
		elif sqr<num:
			left=mid+1#search in right half
		elif sqr>num:
			right=mid-1#search in left half
	return False
print(isPerfectSquare(16))

