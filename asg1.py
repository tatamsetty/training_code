email = "abc.aaa.123@gmail.com"
#email = "abc_3@yahoomail.co.in"
email = "qqq.33____3@testingstuff.us"

print(email)
print(email.find('@'))
at_pos = email.find('@')

print(email[at_pos:])
print(email[at_pos+1:])

cleaned_str_1 = email[at_pos+1:]
cs_dot_pos = cleaned_str_1.find('.')
print(cleaned_str_1[0:cs_dot_pos])