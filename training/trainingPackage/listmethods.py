"""
Built-in methods to help manipulating a list
"""
a,b = 10,20
a= 14
print ('a=%i  and b=%i'%(a,b))
cars = [ "bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("honda")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)

print ('new'*15)

print (cars)
slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

print("*#"*20)
print(cars)
cars.sort()
print(cars)
cars.reverse()

print(cars)

i=[1, 2, 3, 3, 2, 1]
print (i[4:])
print (i[-2:])
print (i[4:6])