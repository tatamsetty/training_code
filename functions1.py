def myFunc():
   print("This message is from the function: myFunc")


myFunc()
myFunc()


def add2nums(n1,n2):  # parameter / arguments
    print(n1+n2)
    
add2nums(n1=100,n2=200)
add2nums(n1=-100,n2=200)
add2nums(100,200)
# add2nums()
# add2nums(,)

a = 100
b = 200
add2nums(a,b)
add2nums(n1='a',n2='a')

def addnums( n1, n2 = 100):
    print(n1+n2)
    
addnums(200)
addnums('a','b')
