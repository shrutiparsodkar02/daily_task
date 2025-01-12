def sumOfSquares(nums):
	length=len(nums)
	res=0
	for i in range(1,length+1):
		if length%i==0:
			ele=nums[i-1]
			res+=ele*ele
			print(res)
	return res
print(sumOfSquares([1,2,3,4]))
