def singleNumber(nums):
	#[2,2,1]
	'''for i in range(len(nums)):
		val=True
		for j in range(len(nums)):
			if i!=j and nums[i]==nums[j]:
				val=False
				break
	if val:
		return nums[i]'''
	result = 0
	for num in nums:
		result ^= num
		print(result)
	return result

print("-->",singleNumber([2,3,2]))
