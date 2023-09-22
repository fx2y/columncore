# lexer.py

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Lexer:
    def __init__(self, input):
        self.input = input
        self.pos = 0
        if len(self.input) == 0:
            self.current_char = None
        else:
            self.current_char = self.input[self.pos]

        self.operators = {
            '>': 'GREATER_THAN',
            '<': 'LESS_THAN',
            '=': 'EQUALS',
            '!=': 'NOT_EQUALS',
            '+': 'PLUS',
            '-': 'MINUS',
            '*': 'MULTIPLY',
            '/': 'DIVIDE'
        }

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.input) - 1:
            self.current_char = None
        else:
            self.current_char = self.input[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def string(self):
        result = ''
        self.advance()
        while self.current_char is not None and self.current_char != "'":
            result += self.current_char
            self.advance()
        self.advance()
        return result

    def identifier(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token('INTEGER', self.integer())

            if self.current_char == "'":
                return Token('STRING', self.string())

            if self.current_char.isalpha():
                return Token('IDENTIFIER', self.identifier())

            if self.current_char in self.operators:
                operator = self.current_char
                self.advance()
                if self.current_char is not None and self.current_char == '=':
                    operator += self.current_char
                    self.advance()
                return Token('OPERATOR', operator)

            if self.current_char == ',':
                self.advance()
                return Token('COMMA', ',')

            if self.current_char == ';':
                self.advance()
                return Token('SEMI', ';')

            self.error()

        return Token('EOF', None)
