__author__ = 'rekhatapdiya'

def sum_all_numbers(myList):
    sum = 0
    for element in myList:
        sum += element
    return sum

print sum_all_numbers([1, 2, 3])
