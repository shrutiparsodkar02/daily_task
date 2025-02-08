def getLucky(s, k):
	val=list(range(1,27))
	symbol=list(chr(i) for i in range(97,123))
	print(symbol)
	print(val)
	val_sym={symbol[i]:val[i] for i in range(26)}
	print(val_sym)
	str_1=""
	for i in s:
		str_1+="".join(str(val_sym[i]))
	for _ in range(k):
		sum_digits = sum(int(char) for char in str_1)
		str_1 = str(sum_digits)
	return int(str_1)
res=getLucky("iiii",1)
print(res)
