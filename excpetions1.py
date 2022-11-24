print(1)
"""
try:
    a=10
    print(a)
    
except:
    print("some error")
    try:
        print(b)
    except:
        print("error in except block")
finally:
    #print("Tinitiate: THIS MESSAGE MUST BE PRINTED")
    try:
        print(b)
    except:
        print("error in finally")
    
print(2)
"""

try:
    # a=10
    # print(a)
    a = 1/0
except Exception as e:
    print(type(e).__name__)
    print(e)
else:
    print("Message from Else Section")
finally:
    print("Message from finally")
    
print(3)
    