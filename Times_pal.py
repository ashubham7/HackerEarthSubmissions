# https://www.hackerearth.com/problem/algorithm/times-pal/

for  i in xrange(input()):
	a ,b = raw_input(), raw_input()
	ans = 0 
	for j in range(len(a)):
		chk  = a[:j] + b + a[j:]
		if  chk == chk[::-1]:
			ans += 1
	temp = a+b
	if temp  == temp[::-1]:
		ans+=1
	print ans