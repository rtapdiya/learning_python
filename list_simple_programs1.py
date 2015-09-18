import sys

"""
1) WAP a function that takes two parameters:
i) list
ii) k
Return True if first element in the list or the last element in the list is k
"""


def exist_element(my_list, variable):
    for idx, element in enumerate(my_list):
        if element == variable:
            if idx == 0 or idx == (len(my_list)-1):
                return True
    return False

print exist_element([1, 2, 3, 4], 4)

"""
2) Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are
 equal

"""


def first_last_element(my_list):
    if len (my_list) > 1:
        list_len = len(my_list)
        for idx,element in enumerate(my_list):
            if my_list[0] == my_list[list_len-1]:
                return True
        return False
    print " enter list of int of size greater than 1"

print first_last_element([1, 2])

"""
3) Find the sum of all elements in the list

"""


def sum_all_numbers(my_list):
    total = 0
    for element in my_list:
        total += element
    return total

print sum_all_numbers([1, 2, -3])

"""
4)Given a list, return True if a number k (given) is in the list "n" times
"""


def isPresent(my_list, k, n):
    occurrence = 0
    for idx,element in enumerate(my_list):
        if element == k:
            occurrence += 1
    if occurrence == n:
        return True
    return False

print isPresent([1, 2, 1, 12, 12, 3], 1, 2)

"""
5)Given 2 int arrays, a and b, each length n where n is odd, return a new array length 2 containing their middle
elements.
Do the same when n is even.  THe resulting list size would be 4, i.e. two middle elements from each list

"""


def find_middle(my_list):
    len_of_list = len(my_list)
    if len_of_list % 2 == 0:
        return my_list[len_of_list / 2 - 1],my_list[len_of_list / 2]
    else:
        return my_list[len_of_list / 2]

print find_middle([1, 2, 3, 4])


def new_middle_list(list1, list2):
    list3 = []
    if len(list1) % 2 == 0:
        element1, element2 = find_middle(list1)
        list3.append(element1)
        list3.append(element2)
        element1, element2 = find_middle(list2)
        list3.append(element1)
        list3.append(element2)
    else:
        list3.append(find_middle(list1))
        list3.append(find_middle(list2))
    return list3

print new_middle_list([1, 2, 3, 4],[4, 5, 6, 7])



"""
7) WAP that returns the maximum and mimimum
"""


def find_max(my_list):
    max_element = my_list[0]
    for idx,element in enumerate(my_list):
        if element > max_element:
            max_element = element
    return max_element

print find_max([1, 23, -9, 0])


def find_min(my_list):
    min_element = sys.maxsize
    for idx,element in enumerate(my_list):
        if element < min_element:
            min_element = element
    return min_element

print find_min([2, 3, -9, -10])

"""
8) WAP that returns the second maximum and second mimimum
"""


def find_second_max(my_list):
    max_element = find_max(my_list)
    my_list.remove(max_element)
    return find_max(my_list)

print find_second_max([10, 20, 30, 40, 90])


def find_second_min(my_list):
    min_element = find_min(my_list)
    my_list.remove(min_element)
    return find_min(my_list)

print find_second_min([10, 20, 30, 40, 90])




