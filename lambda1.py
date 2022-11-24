"""
def Add2Nums(Num1, Num2):
    return Num1+Num2;

# LAMBDA FUNCTION
# Function to Add 2 Numbers
AddLda = lambda x,y: x+y
print(AddLda(1,3))


sequence = [2, 3, 4, 5, 6]
y = list(map(lambda v : v * 5, sequence))

print(y)


def Add2(x):
        return (x+2)

def Add3(x):
        return (x+3)

MyFunctions = [Add2, Add3]

for num in range(5):
    data = list(map(lambda x: x(num), MyFunctions))
    print(data)

"""

from functools import reduce

addData = reduce((lambda x,y:x+y),range(10))
print(addData)

mulData = reduce((lambda x,y:x*y),range(1,10))
print(mulData)