def swap(l,start,end):
	while(start<=end):
		temp=l[start]
		l[start]=l[end]
		l[end]=temp
		start+=1
		end-=1
	return l
def fun(s,d):
	idx=0
	for i in range(len(s)):
		if s[i]==d:
			idx=i
			break
	print(idx)
	s=list(s)
	s=swap(s,0,idx)
	return "".join(s)
	#print(s)
	
word = "abcdefd"
ch = "d"
print(fun(word,ch))
#print(swap([1,2,3,4],0,3))
