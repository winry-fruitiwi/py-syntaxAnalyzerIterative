# demonstration of the in operator in python, which returns a boolean saying
# if the item is inside the list. Apparently this works for strings, numbers,
# and lists, so you can detect nested lists. But you have to get the contents
# right.
my_list = ['a', 'b', 'c', [1], 1, zip([1], [1])]
item = zip([1], [1])
print(item in my_list)


# here I will also implement the "in" operator using a function
# ...hmm I have to use to iterate through my_list. this might be a different
# definition so I'll use it for now
def my_in(search_item, list_to_search):
    for item_to_compare in list_to_search:
        if search_item == item_to_compare:
            return True
    return False


print(my_in(item, my_list))
