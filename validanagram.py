'''def isAnagram( s1, t1):
	lens=len(s1)
	lent=len(t1)
	s=list(s1)
	t=list(t1)
	if(lens==lent):
		for i in range(len(s)):
			for j in range(i+1,len(s)):
				if(s[i]>s[j]):
					temp=s[i]
					s[i]=s[j]
					s[j]=temp
		#print(s)
		for i in range(len(t)):
			for j in range(i+1,len(t)):
				if(t[i]>t[j]):
					temp=t[i]
					t[i]=t[j]
					t[j]=temp
		#print(t)
		if(s==t):
			return True
		else:
			return False
	else:
		return False
res=isAnagram("star","ctar")
print(res)'''
def isAnagram(s,t):
	lens=len(s)
	lent=len(t)
	list_s=list(s)
	list_t=list(t)
	list_s.sort()
	list_t.sort()
	if(lens==lent):
		if(list_s==list_t):
			return True
		else:
			return False
	else:
		return False
res=isAnagram("sing","ring")
print(res)
