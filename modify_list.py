# Implementing the task
# Creating a function to modify list
# Function will not return anything
# It will just modify the list
# All odd numbers will be deleted
# All even numbers will be divided (integer division) by two


# Creating function for modifying list with 'del' method
def modify_list_del(lst):
    # We're going through the list elements but from the end (len(lst) - 1)
    # To the 0 element (-1), with the step -1
    # As we're going to use remove method
    # So not to be out of range
    for i in range(len(lst) - 1, -1, -1):  # range(start, to, step)
        # Checking if the rest from the division by 2 is not 0 (odd number)
        if lst[i] % 2 != 0:
            # Deleting element from the list in the position i with 'del' method
            del lst[i]
        # Else it is even number
        else:
            lst[i] //= 2


# Creating function for modifying list with 'pop' method
def modify_list_pop(lst):
    # Creating an intermediate local list
    a = []
    # We're going through the list elements but from the end (len(lst) - 1)
    # To the 0 element (-1), with the step -1
    # As we're going to use remove method
    # So not to be out of range
    for i in range(len(lst) - 1, -1, -1):  # range(start, to, step)
        # Checking if the rest from the division by 2 is not 0 (odd number)
        if lst[i] % 2 != 0:
            # Deleting element from the list in the last position with 'pop' stack method
            lst.pop()
        # Else it is even number
        else:
            # Adding the element in the last position with 'append' stack method
            a.append(lst[i] // 2)
            # Deleting element from the list in the last position with 'pop' stack method
            lst.pop()
    # As our 'lst' list is empty now but intermediate 'a' list is full,
    # we reassign data from 'a' list to 'lst' list
    for i in range(len(a)):
        lst.append(a[i])
    # Reassigning ready data in revers direction
    lst.reverse()


# Lists for testing
lst_del = [1, 2, 8, 4, 5, 6]
lst_pop = [1, 2, 8, 4, 5, 6]

# Showing the results
print(modify_list_del(lst_del))  # None
print(lst_del)  # [1, 4, 2, 3]

print(modify_list_pop(lst_pop))  # None
print(lst_pop)  # [1, 4, 2, 3]
