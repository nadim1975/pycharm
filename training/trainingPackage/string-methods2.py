"""
Examples to show available string methods in python
"""

# Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC',2))

# Sub-Strings
# starting index is inclusive
# Ending index is exclusive
sub = a[0:6]
step = a[1:6:2]

print("****************")

print(sub)
print(step)

print (a[2:6])
print( a[:])

print (a.replace('c3','Nadim'))


a=5
print (a)

print (a+6)

print (a)