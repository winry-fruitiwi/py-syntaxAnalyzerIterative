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

            # print(stripped_line)

            current_tokens.append(stripped_line)

        for token in current_tokens:
            print(token)

            # if the token is a keyword, print "keyword"
            if token in keywords:
                print("keyword")

            # a string of numbers we encounter
            encountered_number_string = ""

            # a string of strings that we encounter, reset after every second
            # double quote detected
            string_of_string_constants = ""

            # toggle for including letters in string_of_string_constants
            string_constant_fabrication = False

            # for every symbol character in token, print "symbol"
            for letter in token:
                # a letter is not a symbol if it is a string constant
                if letter in symbols and not string_constant_fabrication:
                    print("symbol")

                if string_constant_fabrication:
                    string_of_string_constants += letter

                else:
                    # print(string_of_string_constants)
                    string_of_string_constants = ""

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
                else:
                    if encountered_number_string != "":
                        print(encountered_number_string)

                # if there is a double quote, that means there will be a string
                # until the next double quote
                if letter == '"' and string_constant_fabrication == False:
                    string_constant_fabrication = True

            # spacing between tokens and keywords
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
