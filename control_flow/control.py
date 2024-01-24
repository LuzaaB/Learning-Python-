# default argument values
def say(message, times=1):
    print (message * times)
say('Hello')
say('World',5)

# the 'global' statement
x = 50
def func():
    global x # 'global' keyword is necessary otherwise error
    print ('x is ',x)
    x=2
    print('changed x to ',x)
func()
print('value of x ',x)

# keyword arguments 
def fun(a, b=5, c=10):
    print('a is ',a, ', b is ',b, 'and c is ',c)
fun(3,7)
fun(25, c=100)
fun(c=20, a=90)