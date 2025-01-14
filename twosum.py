def twoSum( nums, target):
        for i in range(len(nums)):
        	for j in range(len(nums)):
        		if((nums[i]+nums[j])==target):
        			nums.pop(i)
        			nums.pop(j)
        			return list[i,j]
 
nums=[3,2,4]
res=twoSum(nums, 6)
print(res)
