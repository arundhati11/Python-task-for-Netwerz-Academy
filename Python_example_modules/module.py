def str_to_list(str1):
	l1 = []
	for i in str1:
		l1.append(i)
	print(l1)
		
		
		
def filter_ca(list1):
	for i in list1:
		if i[0] == 'c' and i[1] == 'a':
			print('True')
		else:
			print('False')
		
def mul_two_num(x,y):
	m = x*y
	return m
	
def sub_three_num(x,y):
	s = x*y
	return s