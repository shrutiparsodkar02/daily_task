def sortColors(nums):
	for i in range(0,len(nums)):
		for j in range(i+1,len(nums)):
			if(nums[i]>=nums[j]):
				nums[i],nums[j]=nums[j],nums[i]
	return nums
nums = [2,0,2,1,1,0]
print(sortColors(nums))
