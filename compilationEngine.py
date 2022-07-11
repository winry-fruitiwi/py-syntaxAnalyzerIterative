class CompilationEngine:
    def __init__(self, jack_input, xml_output):
        pass

    # Compiles a complete class.
    def compile_class(self):
        pass

    # Compiles a static variable or field declaration.
    def compile_class_var_dec(self):
        pass

    # Compiles a complete method/function/constructor.
    def compile_subroutine_dec(self):
        pass

    # Compiles a parameter list. Doesn't handle enclosing parentheses.
    def compile_parameter_list(self):
        pass

    # Compiles a subroutine's body.
    def compile_subroutine_body(self):
        pass

    # Compiles a variable declaration
    def compile_var_dec(self):
        pass

    # Compiles a sequence of statements. Doesn't handle enclosing brackets.
    def compile_statements(self):
        pass

    # Compiles an expression
    def compile_expression(self):
        pass

    # Compiles a term.
    def compile_term(self):
        pass

    # Compiles a comma-separated list of expressions.
    def compile_expression_list(self):
        pass

    # Note that we didn't compile grammar rules such as statement. This is
    # because they're only referenced once in other rules.

    # Note that we didn't compile terminal grammar rules with only constants
    # on the right-hand side because our tokenizer handles this for us.
