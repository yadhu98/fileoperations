class Person:
    def  __init__(self,name):
        def inner():
            print("hi welcome!")
        self.name = name
        self.greet = inner
    
    def greet(self):
        print('Hi {}'.format(self.name))



p = Person('Yadhu')
print(p.greet())
Person.greet(p)
print( p.__dict__)




