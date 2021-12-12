from src import lexer

if __name__ == '__main__':

    user_input = input("> ")

    lexer_ = lexer.Lexer(user_input)

    result = lexer_.tokenize()

    print(result)