class JackTokenizer:
    def __init__(self, jack_input):
        pass

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
