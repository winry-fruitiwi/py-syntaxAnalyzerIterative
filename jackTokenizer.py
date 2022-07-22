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


class JackTokenizer:
    def __init__(self, jack_input_string):
        self.jack_input = open(jack_input_string, "r")

        # read every string and remove whitespace, comments, and newlines.
        current_lines = self.jack_input.readlines()

        # a list of "tokens", but these are only separated by spaces
        current_tokens = []

        # a list of booleans that represent whether I have a keyword
        keyword_booleans = []

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

            print(stripped_line)

            current_tokens.extend(stripped_line.split(' '))

        for token in current_tokens:
            if token in keywords:
                keyword_booleans.append(True)
            else:
                keyword_booleans.append(False)

        print(current_tokens + keyword_booleans)

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
