"""
class ParentClass():
    Parentvar1 = "parentVariable Value"
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")



class ChildClass(ParentClass):
    ChildVar1 = "parentVariable Value"
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")


# Create an object of the Child Class
cObj = ChildClass()


# CALL CHILDCLASS and PARENTCLASS methods from the child object
cObj.childFunction()
cObj.parentFunction()
"""

"""
class Parent_1():
    "This is another parent-level class"

    def Parent1Function(self):
        print("This is a message from the Parent_1.Parent1Function")

class Parent_2():
    "This is another parent-level class"

    def Parent2Function(self):
        print("This is a message from the Parent_2.Parent2Function")

# Class that inherits from 2 parents
class ChildMI(Parent_1, Parent_2):
    "This is the ChildMI, this inherits Parent_1 and Parent_2"

    def ChildMIFunction(self):
        print("This is a message from the ChildMI.ChildMIFunction")


# Create ChildMI Object
gcObj = ChildMI()

gcObj.Parent1Function()
gcObj.Parent2Function()

"""

class GrandParent():
    "This is the GrandParent class"
    def GrandParentFunction(self):
        print("This is a message from the GrandParent.GrandParentFunction")

# This inherits the GrandParent class
class Parent(GrandParent):
    "This is the Parent class"
    def ParentFunction(self):
        print("This is a message from the Parent.ParentFunction")

# Class that inherits Parent Class
class Child(Parent):
    "This is the ChildMI, this inherits Parent_1 and Parent_2"
    def ChildFunction(self):
        print("This is a message from the Child.ChildFunction")

# Create ChildMI Object
gcObj = Child()

gcObj.GrandParentFunction()
gcObj.ParentFunction()
gcObj.ChildFunction()