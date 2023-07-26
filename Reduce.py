#Let's consider a more complex example using the reduce() function to find the maximum word in a list of strings based on their lengths.
from functools import reduce
def findmaxWord(x,y):
    max_value = x if len(x) > len(y) else y
    return max_value
numbers=["a","ab","abc","abcd","f"]
print(reduce(findmaxWord,numbers))