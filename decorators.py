def log(func):
    def wrapper(*args,**kwargs):
        print('args',args,'\n','kwargs',kwargs)
        result = func(*args,**kwargs)
        return result
    return wrapper


@log
def add(a,b=2):
    return a+b

@log
def hello(greeting,name='Alex'):
    print('{} {}!! How are you?'.format(greeting,name))


a = add(2,b=4)
b = hello('Hello',name='Yadhu')

print(a)
print(b)