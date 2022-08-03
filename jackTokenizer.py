# import the regular expressions module!
import re

# a full list of all keyword constants possible
keywords = [
    'class',
    'constructor',
    'function',
    'method',
    'field',
    'static',
    'var',
    'int',
    'char',
    'boolean',
    'void',
    'true',
    'false',
    'null',
    'this',
    'let',
    'do',
    'if',
    'else',
    'while',
    'return'
]

# full list of symbols
symbols = [
    '{',
    '}',
    '(',
    ')',
    '[',
    ']',
    '.',
    ',',
    ';',
    '+',
    '-',
    '*',
    '/',
    '&',
    '|',
    '<',
    '>',
    '=',
    '~'
]

print(re.split("[{}\[\].,;+\-*/&|<>=~]", "{}[].,;+-*/&|<>=~"))

# all possible numbers
numbers = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]


class JackTokenizer:
    def __init__(self, jack_input_string):
        self.jack_input = open(jack_input_string, "r")

        # read every string and remove whitespace, comments, and newlines.
        current_lines = self.jack_input.readlines()

        # a list of "tokens", but these are currently only separated by spaces
        current_tokens = []

        for line in current_lines:
            stripped_line = line.strip(" ").strip("\n").strip(" ")

            if stripped_line[0:2] == "//" or stripped_line == "":
                continue

            try:
                if stripped_line.index("//"):
                    stripped_line = stripped_line[0:stripped_line.index("//")]
                    stripped_line = stripped_line.strip(" ")
            except ValueError:
                pass

            current_tokens.append(stripped_line)

        for line in current_tokens:
            print(line)

            # a string of numbers we encounter
            encountered_number_string = ""

            # a string of strings that we encounter, reset after every second
            # double quote detected
            string_of_string_constants = ""

            # toggle for including letters in string_of_string_constants
            string_constant_fabrication = False

            # the current line without any strings
            line_without_strings = ""

            # for every symbol character in token, print "symbol"
            for letter in line:
                # a letter is not a symbol if it is a string constant
                if letter in symbols and not string_constant_fabrication:
                    print("symbol")

                # if there is a double quote, that means there will be a string
                # until the next double quote
                elif letter == '\"' and not string_constant_fabrication:
                    string_constant_fabrication = True
                elif letter == '\"' and string_constant_fabrication:
                    string_constant_fabrication = False
                    print(string_of_string_constants)
                    string_of_string_constants = ""

                if string_constant_fabrication and letter != '\"':
                    string_of_string_constants += letter
                else:
                    if string_of_string_constants != "":
                        print(string_of_string_constants)
                        string_of_string_constants = ""
                    if letter != '"':
                        line_without_strings += letter

                # otherwise, if the letter is a number, append it to a string
                # of numbers encountered so far
                try:
                    # bug: int() doesn't classify 0 as an int! use for checking
                    # if the letter is not an integer
                    if int(letter) or letter == "0":
                        pass
                    encountered_number_string += letter
                except ValueError:
                    if encountered_number_string != "":
                        print(encountered_number_string)
                        encountered_number_string = ""

            # check for all double quotes and erase everything in between,
            # including the double quotes
            print(line_without_strings)

            # split the token so that we can check for keywords
            split_tokens = line_without_strings.split(" ")

            # split tokens without the extra spaces
            split_tokens_without_extra_spaces = []

            split_tokens = re.split("[{}\[\].,;+\-*/&|<>=~ ]", line_without_strings)

            # if the token is a keyword, print "keyword"
            for split_token in split_tokens:
                symbol_free_token = ""

                for letter in split_token:
                    if letter in symbols or letter in numbers:
                        pass
                    else:
                        symbol_free_token += letter

                if split_token == "":
                    # split_tokens_without_extra_spaces.append(split_token)
                    continue

                split_tokens_without_extra_spaces.append(symbol_free_token)

                print(split_tokens_without_extra_spaces)

            for split_token in split_tokens_without_extra_spaces:
                if split_token in keywords:
                    print("keyword")
                elif split_token in symbols:
                    print("symbol")
                else:
                    print()

                    try:
                        print(re.search("[a-zA-Z_]([0-9a-zA-Z_])*", split_token).group())
                    except AttributeError:
                        pass
            # spacing between tokens and keywords
            print(string_of_string_constants)
            print(encountered_number_string)

            print()

    # Are there more tokens in the input? Returns a boolean.
    def has_more_tokens(self):
        pass

    # Gets the next token from the input, then makes it the current token.
    def advance(self):
        pass

    # Returns either KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, or STRING_CONST.
    # These constants are the types that the current token can have.
    # TODO consider making an enumeration called TokenType?
    def token_type(self):
        pass

    # Functions after this point only return the current token and are only
    # called if they satisfy a current type, except for string_val.

    # Called if the current token type is KEYWORD.
    def key_word(self):
        pass

    # Called if the current token type is SYMBOL.
    def symbol(self):
        pass

    # Called if the current token type is IDENTIFIER.
    def identifier(self):
        pass

    # Called if the current token type is INT_CONST.
    def int_val(self):
        pass

    # Called if the current token type is STRING_CONST, but filters out the
    # double quotes.
    def string_val(self):
        pass
