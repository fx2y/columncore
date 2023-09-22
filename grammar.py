# grammar.py

class Grammar:
    def __init__(self):
        self.keywords = ['SELECT', 'FROM', 'WHERE', 'GROUP BY', 'ORDER BY', 'LIMIT']
        self.operators = {
            '+': ('ADD', 2),
            '-': ('SUB', 2),
            '*': ('MUL', 3),
            '/': ('DIV', 3),
            '%': ('MOD', 3),
            '=': ('EQ', 1),
            '<>': ('NEQ', 1),
            '<': ('LT', 1),
            '<=': ('LTE', 1),
            '>': ('GT', 1),
            '>=': ('GTE', 1),
            'AND': ('AND', 0),
            'OR': ('OR', 0),
            'NOT': ('NOT', 4)
        }
        self.expressions = {
            'literal': ['INTEGER', 'FLOAT', 'STRING', 'NULL'],
            'column': ['IDENTIFIER'],
            'unary': ['ADD', 'SUB', 'NOT'],
            'binary': ['ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE', 'AND', 'OR'],
            'function': ['IDENTIFIER']
        }
        self.statements = {
            'select': ['SELECT', 'FROM', 'WHERE', 'GROUP BY', 'ORDER BY', 'LIMIT'],
            'insert': ['INSERT', 'INTO', 'VALUES'],
            'update': ['UPDATE', 'SET', 'WHERE'],
            'delete': ['DELETE', 'FROM', 'WHERE']
        }
