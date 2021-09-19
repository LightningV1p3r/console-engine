import viperlogger

####################
#Constants
####################

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

####################
#Logger
####################

lexer_logger = viperlogger.Logger("Lexer")
lexer_logger.enable_debugmode('True')
parser_logger = viperlogger.Logger("Parser")

####################
#Errors
####################

class Error:

    def __init__(self, error_name, details) -> None:
        self.error_name = error_name
        self.details = details

    def __repr__(self) -> str:
        return f'{self.error_name}: {self.details}'

class IllegalCharError(Error):

    def __init__(self, details) -> None:
        super().__init__('Illegal Character', details)
        lexer_logger.error(f'{self.error_name}: {self.details}')

####################
#Token
####################

TT_INT = 'TT_INT'
TT_STR = 'TT_STR'
TT_FLAG = 'FLAG'

class Token: 
    def __init__(self, type_, value=None) -> None:
        self.type = type_
        self.value = value

    def __repr__(self) -> str:
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

####################
#Lexer
####################

class Lexer:

    def __init__(self, text: str) -> None:
        lexer_logger.info(f"Started Lexer with input: {text}")
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self) -> None:
        self.pos += 1

        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
            lexer_logger.debug(f"Advanced to character: {self.current_char}")
        else:
            self.current_char = None
            lexer_logger.debug(f"Advanced to character: {self.current_char}")

    def make_tokens(self) -> list:
        lexer_logger.debug("Started tokenizing process")
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in LETTERS:
                tokens.append(self._make_string_())
            elif self.current_char == '-':
                tokens.append(self._make_flag_())
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")

        return tokens, None

    def _make_string_(self) -> Token:
        lexer_logger.debug("generating value for TT_STR")
        string = ''

        while self.current_char != None and self.current_char in LETTERS:

            if self.current_char in ' /t':
                break
            else:
                string += self.current_char
                self.advance()

        lexer_logger.debug(f"generated TT_STR with value: {string}")
        return Token(TT_STR, value=string)

    def _make_flag_(self) -> Token:
        flag = ''

        while self.current_char != None and self.current_char in LETTERS:

            self.advance()

            if self.current_char in ' \t':
                break
            else:
                flag += self.current_char
        
        return Token(TT_FLAG, flag)

    def _check_input_(self):
        pass

####################
#Parser
####################

class Parser:

    def __init__(self) -> None:
        pass