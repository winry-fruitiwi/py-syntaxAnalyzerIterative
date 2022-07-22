# demonstration of the in operator in python, which returns a boolean saying
# if the item is inside the list. Apparently this works for strings, numbers,
# and lists, so you can detect nested lists. But you have to get the contents
# right.
my_list = ['a', 'b', 'c', [1], 1, list(zip([1], [1]))]

item = list(zip([1], [1]))

print(item in my_list)
