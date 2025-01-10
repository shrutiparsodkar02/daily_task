def isPalindrome(s1):
        """
        :type s: str
        :rtype: bool
        """
        s2=[]
        for i in s1:
        	if(i.isalnum()):
        		s2.append(i.lower())
        		
        return s2 == s2[::-1]
res=isPalindrome("0p")
print(res)
