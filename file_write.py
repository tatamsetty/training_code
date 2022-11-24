import os


# STEP 2: Create a file in Write Mode 
new_file = open("D:/Training/output.txt", "w")

"""
# STEP 3: Write to file using write method
new_file.write("Welcome to Tinitiate.COM\n")
new_file.write("Line 2 data\n")
new_file.write("Line 3 data\n")
new_file.write("Oct 19 0445 AM,\n")
"""

#for c1 in range(100,1000):
#    new_file.write(str(c1)+"\n")
    
new_file.write("end")
new_file.close()