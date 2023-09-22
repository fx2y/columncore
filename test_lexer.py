import unittest

from lexer import Lexer, TokenType, Token


class TestLexer(unittest.TestCase):
    def test_tokenize_keywords(self):
        lexer = Lexer('SELECT * FROM my_table WHERE id = 1')
        tokens = lexer.tokenize()
        expected_tokens = [
            Token(TokenType.KEYWORD, 'SELECT'),
            Token(TokenType.OPERATOR, '*'),
            Token(TokenType.KEYWORD, 'FROM'),
            Token(TokenType.IDENTIFIER, 'my_table'),
            Token(TokenType.KEYWORD, 'WHERE'),
            Token(TokenType.IDENTIFIER, 'id'),
            Token(TokenType.OPERATOR, '='),
            Token(TokenType.LITERAL, '1')
        ]
        self.assertEqual([token.type for token in tokens], [token.type for token in expected_tokens])
        self.assertEqual([token.value for token in tokens], [token.value for token in expected_tokens])

    def test_tokenize_identifiers(self):
        lexer = Lexer('SELECT column1, column2 FROM my_table')
        tokens = lexer.tokenize()
        expected_tokens = [
            Token(TokenType.KEYWORD, 'SELECT'),
            Token(TokenType.IDENTIFIER, 'column1'),
            Token(TokenType.OPERATOR, ','),
            Token(TokenType.IDENTIFIER, 'column2'),
            Token(TokenType.KEYWORD, 'FROM'),
            Token(TokenType.IDENTIFIER, 'my_table')
        ]
        self.assertEqual([token.type for token in tokens], [token.type for token in expected_tokens])
        self.assertEqual([token.value for token in tokens], [token.value for token in expected_tokens])

    def test_tokenize_literals(self):
        lexer = Lexer('SELECT * FROM my_table WHERE id = 1.23')
        tokens = lexer.tokenize()
        expected_tokens = [
            Token(TokenType.KEYWORD, 'SELECT'),
            Token(TokenType.OPERATOR, '*'),
            Token(TokenType.KEYWORD, 'FROM'),
            Token(TokenType.IDENTIFIER, 'my_table'),
            Token(TokenType.KEYWORD, 'WHERE'),
            Token(TokenType.IDENTIFIER, 'id'),
            Token(TokenType.OPERATOR, '='),
            Token(TokenType.LITERAL, '1.23')
        ]
        self.assertEqual([token.type for token in tokens], [token.type for token in expected_tokens])
        self.assertEqual([token.value for token in tokens], [token.value for token in expected_tokens])

    def test_tokenize_operators(self):
        lexer = Lexer('SELECT column1 + column2 FROM my_table')
        tokens = lexer.tokenize()
        expected_tokens = [
            Token(TokenType.KEYWORD, 'SELECT'),
            Token(TokenType.IDENTIFIER, 'column1'),
            Token(TokenType.OPERATOR, '+'),
            Token(TokenType.IDENTIFIER, 'column2'),
            Token(TokenType.KEYWORD, 'FROM'),
            Token(TokenType.IDENTIFIER, 'my_table')
        ]
        self.assertEqual([token.type for token in tokens], [token.type for token in expected_tokens])
        self.assertEqual([token.value for token in tokens], [token.value for token in expected_tokens])

    def test_tokenize_invalid_character(self):
        lexer = Lexer('SELECT column1 + column2 FROM my_table WHERE id = 1 AND name = "John"!')
        with self.assertRaises(Exception):
            tokens = lexer.tokenize()


if __name__ == '__main__':
    unittest.main()
