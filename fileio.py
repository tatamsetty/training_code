import os

print(os.getcwd())


my_dir = "D:\\Training"

# Change Directory to the specified name in my_dir
os.chdir(my_dir)

# Check if Current Directory is the one specified in variable "my_dir"
print(os.getcwd())

print(os.listdir(my_dir))

new_dir="D:\\Training/test"
os.mkdir(new_dir)

print(os.listdir(my_dir))
print(os.path.exists(new_dir))
os.rmdir(new_dir)
print(os.path.exists(new_dir))

#print("abc")
#print("abc\"")