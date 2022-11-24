import pickle
from pickle1 import PickleTest


# DeSerialize File to Object
with open('D:\\Training\\object.pickle', 'rb') as f:
	ObjFile = pickle.load(f)

# print(ObjFile)

print(ObjFile.a)
print(ObjFile.b)