# Print even numbers up to 100

for c1 in range(101):  #range(1,101):
    if c1%2==0:
        print(c1)

print("----")

# Print the first N even numbers
N = 300
ctr = 0
num=1
while (ctr < N):

    if num%2==0:
        print(num)
        ctr = ctr+1  # success
        
    num = num + 1    # Always increment
    

"""
curr_value = 0                  # SETUP a condition criteria
while (curr_value < 5):
    curr_value += 1  # same as curr_value = curr_value + 1
    print('Curr_value: ', curr_value)
    
print('=============')
    
curr_value = 0                  # SETUP a condition criteria
while (curr_value < 5):
    print('Curr_value: ', curr_value) 
    curr_value += 1  # same as curr_value = curr_value + 1
"""