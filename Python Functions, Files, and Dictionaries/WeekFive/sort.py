#sorted and sort
L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2) # unchanged

print("----")

L2.sort()
print(L2)
print(L2.sort())  #return value is None

#reverse
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))
#Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]

lst_sorted=sorted(lst,reverse=True)

#ex
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))
# You will be sorting the following list by each element’s second letter, a to z. Create a function to use when sorting, called second_let. It will take a string as input and return the second letter of that string. Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']


def second_let(char):
    return char[1]


sorted_by_second_let = sorted(ex_lst, key=second_let)
# Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input, and returns only its last character. Use this function to sort the list nums by the last digit of each number, from highest to lowest, and save this as a new list called nums_sorted.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']


def last_char(string):
    return string[-1]


nums_sorted = sorted(nums, key=last_char, reverse=True)



#Once again, sort the list nums based on the last digit of each number from highest to lowest. However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda =sorted(nums,reverse=True,key=lambda x:x[-1])
