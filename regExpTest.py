# import re
#
# identifier = "_d_ddhimd1rk"
#
# print(identifier == re.search("[a-zA-Z_]([0-9a-zA-Z_])*", identifier).group())

# an attempt to re-implement re.split

# a list of characters that we want to split by. Special sequences not allowed.
split_list = [
    "'",
    ",",
    "."
]


def reg_exp_split(string_to_split):
    # a set of bounds for the previous and current bounds for our next split
    # item.
    left_bound = 0
    right_bound = 0

    # list of strings that the string will be split into
    list_of_split_strings = []

    for letter in string_to_split:
        if letter in split_list:
            print(letter)

            list_of_split_strings.append(string_to_split[left_bound:right_bound])
            list_of_split_strings.append(letter)
            left_bound = right_bound + 1

        right_bound += 1

    return list_of_split_strings


print(reg_exp_split("Hi, don't touch me, but my name is Blank Slate. Hi!"))
