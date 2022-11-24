"""
# This program demos print to console
print(1)    # Int
print('a')  # String
print(10.1) # Decimal
"""

# variable
a = 1
# print(a)
a1 = 12
A1 = 13
# print(a1)
# print(A1)
# 1a = 12
"""
c = a1
print(c)
print(c+10)
# c = c +10
print(c)
"""
"""
var_test_string = "Python is cool"
print( var_test_string[0])
print( var_test_string[13])
print( var_test_string[0:4])
print( var_test_string[10:])
print( var_test_string[-4:])
print( "Python is cool"[-4:])

print('test'.find('e'))
x = 'test'
print(x.find('e'))
"""

email = "abc.aaa.123@gmail.com"
email = "abc_3@yahoomail.co.in"
email = "qqq.33____3@testingstuff.us"

print(email)
print(email.find('@'))
at_pos = email.find('@')

print(email[at_pos:])
print(email[at_pos+1:])
cleaned_str_1 = email[at_pos+1:]
cs_dot_pos = cleaned_str_1.find('.')
print(cleaned_str_1[0:cs_dot_pos])