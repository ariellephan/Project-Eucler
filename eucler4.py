#!/usr/bin/python
def palindrome(x):
	if x[::-1] == x:
		return 1
max_list = []
max_y_list = []
for x in xrange(1000,100,-1):
	if x in max_y_list:
		break
	for y in xrange(1000,100,-1):
		if (palindrome(str(x*y)) == 1):
			max_list.append(x*y)
			max_y_list.append(y)
print max(max_list)		