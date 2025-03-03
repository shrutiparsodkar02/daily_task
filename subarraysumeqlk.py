def sunarraysum(n,k):
	sum1=0
	l=0
	r=0
	count=0
	while(r<len(n)):
		sum1=sum(n[l:r+1])
		if sum1 <= k-1:
			count+=1
			r+=1
		else:
			l+=1
	return count-1
n = [0,0,0,0,0]
k = 0
print(sunarraysum(n,k))
