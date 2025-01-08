#these code is more optimizes
def trap(height):
	#height=[4,2,0,3,2,5]
	length_height=len(height)
	left_max=[]
	right_max=[]
	res=0
	if length_height>2:
		left_max.append(height[0])
		for i in range(1,length_height):
			#for left_max array
			if left_max[i-1]>height[i]:
				left_max.append(left_max[i-1])
			else:
				left_max.append(height[i])
		#for right_maxarray
		right_max.append(height[length_height-1])
		for i in range(length_height-2,-1,-1):
			#print("***>",height[length_height-1])
			#print("////'''",right_max[-1])
			if right_max[-1]>height[i]:
				right_max.append(right_max[-1])
			else:
				right_max.append(height[i])
			#print(i-1)
		right_max.reverse()
		#print(right_max)
		#print(left_max)
		for i in range(length_height):
			min_ele=min(left_max[i],right_max[i])
			cal=min_ele-height[i]
			if cal >= 0:
				res+=cal
			else:
				res+=0
			#print(res)
		return res
	else:
		return 0
print(trap([4,2,0,3,2,5]))
"""def trap(height):
    length_height = len(height)
    
    if length_height < 3:
        return 0  # If there are fewer than 3 bars, no water can be trapped

    left_max = []
    right_max = []
    
    # Initialize left_max and right_max
    left_max.append(height[0])
    right_max.append(height[-1])
    
    # Fill left_max array
    for i in range(1, length_height):
        left_max.append(max(left_max[i-1], height[i]))
    
    # Fill right_max array
    for i in range(length_height-2, -1, -1):
        right_max.append(max(right_max[-1], height[i]))
    
    # Reverse right_max to match the indices of left_max
    right_max.reverse()

    # Now calculate trapped water
    trapped_water = 0
    for i in range(length_height):
        # Water trapped at each index is min(left_max[i], right_max[i]) - height[i]
        trapped_water += min(left_max[i], right_max[i]) - height[i]
    
    return trapped_water

# Example usage
print(trap([4, 2, 8, 3, 2, 1]))
"""
