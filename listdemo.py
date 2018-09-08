"""
Data type to store more than one value in one variable name
List items are in brackets, separated with "," [ 1, 2, 3 ]
"""

cars = [ "bmw", "honda", "audi"]
empty_list = []
print(empty_list)
print(cars)

print("*#"*20)

print(cars[1])

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]

print(sum_num)

more_cars = [ "bmw", "honda", "audi"]
print(more_cars[1])

more_cars[1] = "Benz"

print(more_cars[1])
print(more_cars)

print ('Nadim'*20)

a=['laila','leen','kareem']

print ('my daughters are %s and %s and my son is %s'%(a[0],a[1],a[2]))

a[0]='Noor'

print('my wife is %s'%(a[0]))