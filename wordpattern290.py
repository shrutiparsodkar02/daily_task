def wordPattern(pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s2=[]
        s1=s.split()
        val={"a":"dog","b":"cat"}
        if len(pattern) != len(s1):
            return False
        else:
            for i in pattern:
                s2.append(val[i])
            s3=" ".join(s2)
            print(type(s3))
            return s3==s
pattern = "abba"
s = "dog cat cat dog"
wordPattern(pattern, s)
