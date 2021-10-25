import random
import sys

def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
        return True
def bogo_sort(values):
    count=0   
    while not is_sorted:
        print(count)
        random.shuffle(values)    
        count+=1
    return values

numbers = 1,2,3,9,8,6,7,5
a =bogo_sort(numbers)
print(a)