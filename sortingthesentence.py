def sortSentence(s):
        """
        :type s: str
        :rtype: str
        """
        '''
        #s = "is2 sentence4 This1 a3"
        words=s.split()
        l1=list(words)
        l1.sort()
        #print(l1)
        i=0
        while(i<len(l1)):
        	j=0
        	strn=l1[i];
        	while(j<len(l1[i])):
        		if(l1[j].isdigit):
        			list(l1[i]).pop();
        		j+=1
        	i+=1
        print(l1)
s="is2 sentence4 This1 a3"
res=sortSentence(s)
'''
def sortSentence(s):
	words = s.split()
	words.sort()
	final_words = []
	for i in words:
		cleaned_word = ""
		for j in i:
			if j.isdigit():
				index = int(j)
			else:
				cleaned_word += j
		final_words.insert(index - 1, cleaned_word)
	return ' '.join(final_words)

s = "is2 sentence4 This1 a3"
res = sortSentence(s)
print(res)

