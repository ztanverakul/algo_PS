def G(n):
	if (n==0):
		return int('1')
	elif (n==1):
		return int('-1')
	elif (n==2):
		return int('2')
	else:
		return(int(G(n-1))*int(G(n-2)) + int(G(n-3)))

print (G(10))
