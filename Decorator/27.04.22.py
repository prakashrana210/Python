
#....add dacorator

def func(spam):
    def wrapper(*args, **kwargs):
        return spam(*args, **kwargs) + 5
        #res = spam(*args, **kwargs)  #we can also write like this
        #return res + 5
    return wrapper
@func
def add(a):
    return a

print(add(5))


args = ([1234567890, 9087654738, 911234567890, 231234567890])

res = " "
for i in args:
    if len(i) == 12 and i[:2] != 91:
        str(i).replace(i[:2], '+91-')

    elif len(i) == 10:
        str(i) + "+91"



