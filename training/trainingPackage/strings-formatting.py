"""
Examples to show how string formatting works in python
"""

city = "nyc"
event = "show"
num= 2018

print("Welcome to " + city + " and enjoy the " + event)
print("Welcome to %s" % city)
print("Welcome to %s and enjoy the %s" % (city, event))

print ('welcome to year %f and enjoy %s'% (num,event))

a = "one,two,three"

g = (a.split(','))


print (g[0])