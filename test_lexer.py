# test_lexer.py

import unittest

from lexer import Lexer, Token


class TestLexer(unittest.TestCase):

    def test_integer(self):
        lexer = Lexer('123')
        token = lexer.get_next_token()
        self.assertEqual(token.type, 'INTEGER')
        self.assertEqual(token.value, 123)

    def test_string(self):
        lexer = Lexer("'hello'")
        token = lexer.get_next_token()
        self.assertEqual(token.type, 'STRING')
        self.assertEqual(token.value, 'hello')

    def test_identifier(self):
        lexer = Lexer('SELECT')
        token = lexer.get_next_token()
        self.assertEqual(token.type, 'IDENTIFIER')
        self.assertEqual(token.value, 'SELECT')

    def test_comma(self):
        lexer = Lexer(',')
        token = lexer.get_next_token()
        self.assertEqual(token.type, 'COMMA')
        self.assertEqual(token.value, ',')

    def test_semi(self):
        lexer = Lexer(';')
        token = lexer.get_next_token()
        self.assertEqual(token.type, 'SEMI')
        self.assertEqual(token.value, ';')

    def test_eof(self):
        lexer = Lexer('')
        token = lexer.get_next_token()
        self.assertEqual(token.type, 'EOF')
        self.assertEqual(token.value, None)

    def test_complex_query(self):
        query = "SELECT name, age FROM users WHERE age > 18;"
        lexer = Lexer(query)

        tokens = [
            Token('IDENTIFIER', 'SELECT'),
            Token('IDENTIFIER', 'name'),
            Token('COMMA', ','),
            Token('IDENTIFIER', 'age'),
            Token('IDENTIFIER', 'FROM'),
            Token('IDENTIFIER', 'users'),
            Token('IDENTIFIER', 'WHERE'),
            Token('IDENTIFIER', 'age'),
            Token('OPERATOR', '>'),
            Token('INTEGER', 18),
            Token('SEMI', ';'),
            Token('EOF', None)
        ]

        for token in tokens:
            next_token = lexer.get_next_token()
            self.assertEqual(next_token.type, token.type)
            self.assertEqual(next_token.value, token.value)
