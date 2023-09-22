from enum import Enum


# Define an enumeration of token types
class TokenType(Enum):
    KEYWORD = 1
    IDENTIFIER = 2
    OPERATOR = 3
    LITERAL = 4


# Define a class to represent a token
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


# Define a class to tokenize SQL queries
class Lexer:
    # Define a set of SQL keywords
    KEYWORDS = {'SELECT', 'FROM', 'WHERE', 'AND', 'OR', 'NOT', 'ORDER', 'BY', 'GROUP', 'HAVING', 'LIMIT', 'OFFSET'}
    # Define a set of SQL operators
    OPERATORS = {'+', '-', '*', '/', '=', '<', '>', '<=', '>=', '<>', '!=', '(', ')', ',', '.', ';'}

    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.tokens = []

    # Tokenize the input string and return a list of tokens
    def tokenize(self):
        while self.pos < len(self.input):
            if self.input[self.pos].isspace():
                # Skip whitespace
                self.pos += 1
            elif self.input[self.pos].isalpha() or self.input[self.pos] == '_':
                # Parse an identifier
                start_pos = self.pos
                while self.pos < len(self.input) and (
                        self.input[self.pos].isalpha() or self.input[self.pos].isdigit() or self.input[
                    self.pos] == '_'):
                    self.pos += 1
                value = self.input[start_pos:self.pos]
                if value.upper() in self.KEYWORDS:
                    # If the identifier is a keyword, create a KEYWORD token
                    self.tokens.append(Token(TokenType.KEYWORD, value.upper()))
                else:
                    # Otherwise, create an IDENTIFIER token
                    self.tokens.append(Token(TokenType.IDENTIFIER, value))
            elif self.input[self.pos].isdigit():
                # Parse a numeric literal
                start_pos = self.pos
                while self.pos < len(self.input) and self.input[self.pos].isdigit():
                    self.pos += 1
                if self.pos < len(self.input) and self.input[self.pos] == '.':
                    self.pos += 1
                    while self.pos < len(self.input) and self.input[self.pos].isdigit():
                        self.pos += 1
                value = self.input[start_pos:self.pos]
                self.tokens.append(Token(TokenType.LITERAL, value))
            elif self.input[self.pos] in self.OPERATORS:
                # Parse an operator
                self.tokens.append(Token(TokenType.OPERATOR, self.input[self.pos]))
                self.pos += 1
            else:
                # Raise an exception for invalid characters
                raise Exception('Invalid character: ' + self.input[self.pos])
        return self.tokens
