# test_grammar.py

import unittest

from grammar import Grammar


class TestGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = Grammar()

    def test_keywords(self):
        self.assertIn('SELECT', self.grammar.keywords)
        self.assertIn('FROM', self.grammar.keywords)
        self.assertIn('WHERE', self.grammar.keywords)
        self.assertIn('GROUP BY', self.grammar.keywords)
        self.assertIn('ORDER BY', self.grammar.keywords)
        self.assertIn('LIMIT', self.grammar.keywords)

    def test_operators(self):
        self.assertIn('+', self.grammar.operators)
        self.assertIn('-', self.grammar.operators)
        self.assertIn('*', self.grammar.operators)
        self.assertIn('/', self.grammar.operators)
        self.assertIn('%', self.grammar.operators)
        self.assertIn('=', self.grammar.operators)
        self.assertIn('<>', self.grammar.operators)
        self.assertIn('<', self.grammar.operators)
        self.assertIn('<=', self.grammar.operators)
        self.assertIn('>', self.grammar.operators)
        self.assertIn('>=', self.grammar.operators)
        self.assertIn('AND', self.grammar.operators)
        self.assertIn('OR', self.grammar.operators)
        self.assertIn('NOT', self.grammar.operators)

    def test_expressions(self):
        self.assertIn('literal', self.grammar.expressions)
        self.assertIn('column', self.grammar.expressions)
        self.assertIn('unary', self.grammar.expressions)
        self.assertIn('binary', self.grammar.expressions)
        self.assertIn('function', self.grammar.expressions)

    def test_statements(self):
        self.assertIn('select', self.grammar.statements)
        self.assertIn('insert', self.grammar.statements)
        self.assertIn('update', self.grammar.statements)
        self.assertIn('delete', self.grammar.statements)
