def sumOddLengthSubarrays(arr):
	sum1=0
	#add=0
	for i in range(len(arr)):
		count=0
		add=0
		for j in range(i,len(arr)):
			print(arr[j])
			add+=arr[j]
			print("add->",add)
			count+=1
			print(count)
			if count%2==1:
				sum1+=add
				print("sum1--->",sum1)
				print("-------------------------------------------------")
		print("******")
	return sum1
print(sumOddLengthSubarrays([10,11,12]))
