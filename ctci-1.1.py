'''
Cracking the Coding Interview
Problem 1.1
Is Unique.  Implement an algorithm to determine if a string has all unique
characters.  What if you cannot use additional structures?

Notes
1.  First thought was to create a nested for loop and compare character in first
for loop with the n +1 character in the second for loop.  In the worst case
though this results in O(sqr(x)).  Most of the time this wouldn't be an issue as
most strings would be language based strings bound by a languages characterset.
Strings though representative of the entire unicode space would be problematic.
This version can be seen in the is_unique_1() function.  This type of function
does not require a secondary data structure to be created.

2.  My second thought was to treat the problem as a sorting problem and sort the
string using a binary sort.  When doing an insertion into the new ordered set
I could check adjacent characters.  If any adjacent character was equal to the
character being inserted the string is not unique.  This drives down performance
to O(log n).  Also, since strings in Python are not mutable any sorting mandates
a new data structure.  This can be seen in the is_unique_2() function below.
'''

import time
import random


def is_unique_1(string):
    start_time_func = time.time()
    unique = True
    for i,char1 in enumerate(string):
        # in the first for loop I enumerate because I don't have to check any
        # character before the character being checked as that set of prior
        # characters has already been checked in the first for loop.  As well I
        # am trying to avoid false duplicate detection by comparing the c1
        # character to itself as c2.
        if i != len(string) - 1:
            for char2 in string[i+1:]:
                if char1 == char2:
                    unique = False
                    end_time_func = time.time()
                    return (end_time_func - start_time_func, unique)
    end_time_func = time.time()
    return (end_time_func - start_time_func, unique)

def is_unique_2(string):
    start_time_func = time.time()
    def find_index(ol, character, upper_bound, lower_bound):
        new_bound = ((upper_bound - lower_bound)/2) + lower_bound
        if ol[new_bound] == character:
            return -1
        elif character < ol[new_bound]:
            if character == ol[new_bound - 1]:
                return -1
            elif character > ol[new_bound - 1]:
                return new_bound
            else:
                return find_index(ol, character, new_bound, lower_bound)
        elif char > ol[new_bound]:
            if character == ol[new_bound + 1]:
                return -1
            elif character < ol[new_bound + 1]:
                return new_bound + 1
            else:
                return find_index(ol, character, upper_bound, new_bound)
    unique = True
    ordered_list = [string[0],]
    for char in string[1:]:
        if char == ordered_list[0] or char == ordered_list[-1]:
            unique = False
            end_time_func = time.time()
            return (end_time_func - start_time_func, unique)
        elif char < ordered_list[0]:
            ordered_list.insert(0, char)
        elif char > ordered_list[-1]:
            ordered_list.append(char)
        else:
            new_index = find_index(
                ordered_list,
                char,
                len(ordered_list) - 1,
                0,
            )
            if new_index < 0:
                unique = False
                end_time_func = time.time()
                return (end_time_func - start_time_func, unique)
            else:
                ordered_list[new_index] = char
    end_time_func = time.time()
    return (end_time_func - start_time_func, unique)


if __name__ == '__main__':
    # Generate large set of unicode characters
    s = []
    for i in range(1, 100000):
        s.append(unichr(i))
    random.shuffle(s)
    s_unique = ''.join(s)
    s.append(u'?')
    s.append(u'?')
    random.shuffle(s)
    s_duplicate = ''.join(s)

    print('unique.')
    result1 = is_unique_1(s_unique)
    print(result1[1], result1[0])
    result3 = is_unique_2(s_unique)
    print(result3[1], result3[0])
    print()

    print('not unique.')
    result2 = is_unique_1(s_duplicate)
    print(result2[1], result2[0])
    result4 = is_unique_2(s_duplicate)
    print(result4[1], result4[0])