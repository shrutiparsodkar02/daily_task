def searchInsert(nums, target):
    if target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
    else:
        i = 0
        while i < len(nums) and target > nums[i]:
            i += 1
        return i

nums = [1, 2, 4, 5]
res = searchInsert(nums, 6)
print(res)

