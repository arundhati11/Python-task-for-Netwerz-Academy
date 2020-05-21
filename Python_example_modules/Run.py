import add
#import add as a  #alias
#from add import even_odd   
#from add import add_two_num
import module 


sum = add.add_two_num(10,5)
print('Sum of two numbers is: ',sum)


sum1 = add.add_three_num(10,5,10)
print('Sum of three numbers is :',sum1)

print('List1 = ',add.list1)

print('Dict = ',add.dict1)

print('Last name = ',add.dict1['Last_name'])

print('Hobbies = ',add.dict1['Hobbies'])

list1 = [1,2,3,4,5,6,7,8,9]
add.even_odd(list1)

'''

sum1 = a.add_two_num(2,3)
print("sum = ",sum1)

print('Dict = ',a.dict1)



'''

'''list1 = [1,2,3,4,5,6,7,8,9]
even_odd(list1)
sum = add_two_num(15,15)
print('Sum of two numbers is: ',sum)
'''

str1 = 'Welcome to python'
module.str_to_list(str1)

l1 = ['cat','car','ball','cure','feather','care','cow']
module.filter_ca(l1)

mul = module.mul_two_num(6,5)
print('Product of two numbers is: ',mul)


sub = module.sub_three_num(7,5,3)
print('Difference of three numbers is: ',sub)