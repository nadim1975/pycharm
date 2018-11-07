class Fruit(object):
    def __init__(self):
        print('init fruit')

    def nutrition(self):
        print('vitamin')

    def fruit_shape(self):
        print('curved')


class Banana(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print ('init Banana')

    def nutrition(self):
        super(Banana, self).nutrition()
        print ('C')

    def color(self):
        print ('yellow')
f= Fruit()
f.nutrition()
f.fruit_shape()
print ('$$$$'*30)
b = Banana()
b.nutrition()
b.color()
b.fruit_shape()
