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


""" sum of all numbers with even index, and sum of all numbers with odd index """
def sum_odd_even_index(my_list):
    sum_odd=0
    sum_even=0
    for idx,element in enumerate(my_list):
        if idx%2 == 0:
            sum_even+=element
        else:
            sum_odd+=element
    return sum_even, sum_odd

print sum_odd_even_index([10,20,30])


""" ZIP of two list """


def zip_list(list1,list2):
    list3 = []

    # A NEW WAY OF DOING THIS:
    # same as if not list1: return list2.  WHich internally is evaluated as if not bool(list1)
    if list1 is None or len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1


    if len(list1)>len(list2):
        size_of_bigger_list = len(list1)
    else:
        size_of_bigger_list=len(list2)

    # A NEW WAY OF DOING THIS:
    # size_of_bigger_list = len(list1) if len(list1) > len(list2) else len(list2)

    counter = 0
    while counter < size_of_bigger_list:
        if counter < len(list1) and counter < len(list2):
            list3.append(list1[counter])
            list3.append(list2[counter])
        if counter >= len(list1):
            list3.append(list2[counter])
        if counter >= len(list2):
            list3.append(list1[counter])
        counter += 1
    return list3


    # for idx,element in enumerate(list1):
    #     for jdx,value in enumerate(list2):
    #
    #         if idx == jdx:
    #             list3.append(element)
    #             list3.append(value)
    #         if jdx < idx and jdx == len(list2)-1:
    #             list3.append(element)
    #         if idx == len(list1)-1 and jdx > idx:
    #             list3.append(value)
    #
    # return list3

print zip_list([1,3,8],[4,6,7,8])


def merge_list(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    l1_index,l2_index = (0,)*3
    l3 = []
    while l1_index<len(l1) and l2_index<len(l2):
        value1 = l1[l1_index]
        value2 = l2[l2_index]
        if value1 == value2:
            l3.append(value1)
            l3.append(value2)
            l1_index += 1
            l2_index += 1
        elif value1 < value2:
            l3.append(value1)
            l1_index += 1
        else:
            l3.append(value2)
            l2_index += 1
    if l1_index < len(l1):
        l3 += l1[l1_index:]
    if l2_index < len(l2):
        l3 += l2[l2_index:]
    return l3

print merge_list([100,101],[1,2,3])




