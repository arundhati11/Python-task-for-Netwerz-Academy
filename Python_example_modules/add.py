def add_two_num(x,y):
	z = x+y
	return z
	
def add_three_num(x,y,z):
	sum = x+y+z
	return sum
	
list1 = [0,2,4,6,8,10,12,14,16,18,20]

dict1 = {
	'First_name': 'Arundhati',
	'Last_name': 'Sarkar',
	'Hobbies' : ['Singing','dancing','painting']
}

def even_odd(l1):
	for num in l1:
		if(num%2==0):
			print('Even')
		else:
			print('Odd')