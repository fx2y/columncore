from lexer import Lexer


def parse_query(query):
    lexer = Lexer(query)
    tokens = lexer.tokenize()
    # TODO: Implement AST generation
    return tokens


if __name__ == '__main__':
    query = 'SELECT * FROM my_table WHERE id = 1'
    ast = parse_query(query)
    print(ast)
