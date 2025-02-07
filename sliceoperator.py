def slice(obj,slice_parameter):
	typ=type(obj)
	#print(typ)
	default_return="' '"
	conv_list = list(obj)  # Convert the object to a list
	start, end, step = None, None, None
# Determine which slice parameters are provided
	if len(slice_parameter) == 1:
		start = slice_parameter[0]
		end = len(conv_list)  # default end to the length of the object
		step = 1  # default step to 1
	elif len(slice_parameter) == 2:
		start = slice_parameter[0]
		end = slice_parameter[1]
		step = 1  # default step to 1
	elif len(slice_parameter) == 3:
		start = slice_parameter[0]
		end = slice_parameter[1]
		step = slice_parameter[2]
	print("inbuilt-->",obj[start:end:step])
	if step ==0:
		raise ValueError ("step cannot be zero")
	elif start == " " and end == " " and step == -1:
		conv_list.reverse()
		return conv_list
	elif slice_parameter==[]:
		return obj
	else:
		res=[]
		if start==len(obj):
			start=(slice_parameter[0])-1
			#print(start)
		if end==0:
			end=slice_parameter[1]-1
			#print(end)
		#print("start-->",start)
		#print("end-->",end)
		#print("step-->",step)
		if start < -1*(len(conv_list)):
			dif=-1*len(conv_list)-(start)
			#print(dif)
			i=0
			while(i<dif):
				start=start+1
				i+=1
			#print("start value in 1-->",start)
		if end>len(conv_list):
			end=len(conv_list)
		'''for i in range(start,end,step):
			res+=conv_list[i]
			#print(conv_list[i])
		return res'''
		if end<0:
			end=end+len(conv_list)
		if start<0:
			start=start+len(conv_list)
			#print("start value in 2-->",start)
		for j in range(start,end,step):
			res+=conv_list[start]
			start+=step
		if typ is str:
			return ''.join(res)
		elif typ is list:
			return res
		elif typ is tuple:
			return tuple(res)
	return default_return
obj=("abcdefghi")
#obj = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
#obj = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
slice_parameter=(4,4,-1)
#slice_parameter=[]
res=slice(obj,slice_parameter)
print("my slice operator--->",res)
