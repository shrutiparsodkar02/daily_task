def search(nums, target):
	for i in range(len(nums)):
		if target==nums[i]:
			return i
	return -1
print(search([4,5,6,7,0,1,2],0))
