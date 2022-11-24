"""
myList = [1, 2, 3, 4, 5]
for element in myList:
    print(element)  # Prints all the elements in new line
    
print("====")    

for c in range(5):
    print('Loop Count: ',c) # Index starts from ZERO !
    
print("====")

for c in range(1,6):
    print('Loop Count: ',c) # Index starts from ZERO !
    
for element_index in range(len(myList)):
    print(myList[element_index])  
"""

for outer_loop in range(5):
    for inner_loop in range(5):
        print(outer_loop, '-', inner_loop) 
        
"""
# LOOP Over the number of characters in a sting
for character in 'MyString':
    print(character) # Prints all the characters in new line

# SYNTAX 1: LOOP over elements in a LIST
myList = [1, 2, 3, 4, 5]
for element in myList:
    print(element)  # Prints all the elements in new line

# SYNTAX 2: LOOP over elements in a LIST
for element_index in range(len(myList)):
    print(myList[element_index])  # Prints all the elements in new line

# Loop through a sub set of list of elements
for element in myList[2:4]:
    print(element)  # Prints all the elements in new line
"""