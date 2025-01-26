def shortestPalindrome(s):
	if s[::]==s[::-1]:
		print("in 1")
		return s
	elif len(s)%2==1:
		s1=s[::-1]
		return s1+s
	elif len(s)%2==0:
		s1=s[::-1]
		return s1[0:-1]+s
print(shortestPalindrome("aacecaaa"))

