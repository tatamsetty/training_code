"""
MyNumbersList = [1, 100, 9, 99]
MyStringList  = ["A", 'b', 'Hello', "This"]

# An Empty list
MyList = []
a = 1
print(a)
print(MyNumbersList)
print(MyNumbersList[0])
print(MyStringList)
print(MyList)


a = [1,'a',2,'b']
print(a)
print(a[2])

a.append(1)
print(a)

a.extend([1,2,3,4])
print(a)
"""
"""
TestList=[1,2,3]
print(TestList)
TestList.insert(0,99)
print(TestList)


TestList=[]
TestList.insert(10,99)
print(TestList)
TestList.insert(90,90)
print(TestList)
"""

newList = [3, 2, 5, 1, 4, 4]

# Length of the LIST
# ------------------
print(len(newList))   # OUTPUT: 6
print(len([1, 2, 3])) # OUTPUT: 3

# get Min and Max element in the list
print(min(newList))  # OUTPUT: 1
print(max(newList))  # OUTPUT: 5
print(sum(newList))  # OUTPUT: 19

# Sort a list
# -----------
newList.sort()
print(newList)  # OUTPUT: [1, 2, 3, 4, 4, 5]

newList.reverse()
print(newList)

# Count the occurrences on the passed element
# -------------------------------------------
print(newList.count(4)) # OUTPUT: 2

x = ['s','P','A','a']
x.sort()
print(x)
print(x[0])