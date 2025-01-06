def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
        	for j in range(i+1,len(s)):
        		if(ord(s[i])==40 and ord(s[j])==41 or ord(s[j])==40 and ord(s[i])==41 ):
        			return True
        		elif(ord(s[i])==91 and ord(s[j])==93 or ord(s[j])==91 and ord(s[i])==93):
        			return True
        		elif(ord(s[i])==123 and ord(s[j])==125 or ord(s[j])==123 and ord(s[i])==125):
        			return True
        		else:
        			return False
s="( [] )"
res=isValid(s)
print(res)     			
        	
       		
        	
