'''def myAtoi(s):

	s=s.lstrip()
	s1=""
	ch="-"
	sign=-1 if s[0]==ch else 1
	if(s[0]=="-"):
		s=s[1:]
        	
	for i in range(len(s)):
		if(s[i].isdigit()):
			s1+=s[i]
		else:
			break
	print(s1)
	if(s1[0].isdigit()):
		s1=int(s1)
	s1*=sign
       
	if(s1<pow(2,31)):
		s1=s1//pow(2,31)
		return s1
	elif(s1>pow(2,31)-1):
		s1=s1//pow(2,31)-1
		return s1
	else:
		return s1
        
s="0-1"
res=myAtoi(s)
print(res)
'''
#ques.8
def myAtoi( s):
        s = s.lstrip() 
        if not s:
            return 0
        
        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        s1 = ""
        for i in range(len(s)):
            if s[i].isdigit():
                s1 += s[i]
            else:
                break
        
        if not s1:  
            return 0
        
        s1 = sign * int(s1)  
        
        
        int_max = 2147483647
        int_min = -2147483648
        if s1 < int_min:
            return int_min
        elif s1 > int_max:
            return int_max
        else:
            return s1
s="0-1"
res=myAtoi(s)
print(res)       	
