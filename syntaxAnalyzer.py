# @author Winry
# @date 2022.7.11
# py-jackAnalyzer coding plans - bytelist
#
# ☒ create project
# ☒ create shell of all classes
# ☒ fill in constructor and read file
# ☒ fill in constructor, read file, remove comments/whitespace
# ☒ remove inline comments as well. used index() instead of find()
# ☒ create current token and separate each token by a space
# ☒ print all the tokens
# ☒ create dictionary of all terminal rules
# ☐ iterate through all chars in token, check for additional tokens
# ☐ identify terminal and non-terminal rules (dict lookup)
# ☐ identify types of terminal rules
# NOTE: currently in test.jack I only have variable declarations
# ☐ always compile a variable declaration with all these steps
# 	NOTE: each of these variable declarations will start with let
# ☐ change test.jack to contain an empty while true loop

# import statements here
from jackTokenizer import JackTokenizer

# we can handle the other three types in our program.

# identify current file/directory here

# create the tokenizers and compilation engines here
tokenizer = JackTokenizer("test.jack")

# While loop for if there are more tokens
