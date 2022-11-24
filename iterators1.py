"""
data_set1 = [11,22,33,44,55]

# Loop or Iterate over this data list using a Loop
for value1 in data_set1:
    print(value1)

# Loop or Iterate over this data list using an Iterator
# Create an iterator using the iter function
itr = iter(data_set1)
print("----")
# Call the print to display the next value
print(itr.__next__())
# some code logic
print(itr.__next__())
# some code logic
# some code logic
# some code logic
print(itr.__next__())
# some code logic
# some code logic
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
"""


class EvenOddNumbers:

    def __init__(self, max):
        self.max = max
        self.number = 0


    # Return the custom __next__ value specified within this function
    def __next__(self):
    
        # Increment the self.number  once everytime the __next__() is called
        self.number += 1

        # Exit when the iterations reach the MAX defined in the constructor
        if self.number > self.max:
            print("Max Number of Iterations reached: ", self.max)
        else:
            
            # Check if the CURRENT number is EVEN or ODD and report it
            if self.number%2 != 0:
                print(str(self.number),"is Odd Number")
            else:
                print(str(self.number),"is Even Number")
            
x = EvenOddNumbers(6)
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()


