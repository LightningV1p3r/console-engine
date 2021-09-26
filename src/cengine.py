# Copyright (c) 2021 LightningV1p3r

####################
#Libs
####################

import viperlogger

####################
#Logger
####################

lexer_logger = viperlogger.Logger("Lexer")
lexer_logger.enable_debugmode('True')

parser_logger = viperlogger.Logger("Parser")
parser_logger.enable_debugmode('True')

####################
#Constants
####################

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'

####################
#Errors
####################

class Error:

    def __init__(self, name, details) -> None:
        self.name = name
        self.details = details


    def __repr__(self) -> str:
        return f"{self.name}: {self.details}"

class IllegalCharError(Error):

    def __init__(self, details) -> None:
        super().__init__('Illgal Character', details)

####################
#Tokens
####################

TT_STR      = 'STR'
TT_INT      = 'INT'
TT_FLOAT    = 'FLOAT'
TT_MINUS    = 'MINUS'
TT_PLUS     = 'PLUS'
TT_SLASH    = 'SLASH'
TT_ASTERISK = 'ASTERISK'
TT_DOT      = 'DOT'
TT_BANG     = 'BANG'
TT_FILE     = 'FILE'
TT_FlAG     = 'FLAG'
TT_PATH     = 'PATH'
TT_IPADDR   = 'IPADDR'

class Token:

    '''Token Object used by Lexer.'''

    def __init__(self, type_, value=None) -> None:
        self.type = type_
        self.value = value


    def __repr__(self) -> str:
        if self.value:
            return f'{self.type}: {self.value}'
        else:
            return f'{self.type}'


####################
#Lexer
####################

class Lexer:

    """Iterates through given input and splits it into tokens."""

    def __init__(self, text) -> None:
        
        lexer_logger.debug(f"To tokenize: '{text}'")
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()


    def advance(self, iterations=1) -> None:

        """Advances the cursor by one char in the input."""

        iter_count = 0

        while iter_count < iterations:

            self.pos += 1

            if self.pos < len(self.text):
                self.current_char = self.text[self.pos]
                lexer_logger.debug(f"Advanced to pos {self.pos} with value: '{self.current_char}'")
            else:
                self.current_char = None

            iter_count += 1
     
        
    def reverse(self, iterations=1) -> None:
         
        """Reverses the cursor by one char in the input."""

        iter_count = 0

        while iter_count < iterations:

            self.pos -= 1

            if self.pos < 0:
                self.pos += 1
                lexer_logger.error('Failed to reverse pos due to invalid index!')
            else:
                self.current_char = self.text[self.pos]
                lexer_logger.debug(f"Reversed to pos {self.pos} with value: '{self.current_char}'")

            iter_count += 1


    def tokenize(self) -> list:
        
        """Start the process of tokenizing."""

        tokens = []

        while self.current_char != None:
            
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in LETTERS:
                tokens.append(self.make_string())
            elif self.current_char in DIGITS:
                res = self.checkforip()
                if res == True:
                    tokens.append(self.make_ipaddr())
                else:
                    tokens.append(self.make_number())
            elif self.current_char == '-':
                self.advance(2)
                if self.current_char in ' \t':
                    self.reverse()
                    tokens.append(self.make_flag())
                else:
                    self.reverse(2)
                    tokens.append(Token(TT_MINUS))
                    self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '/':
                res = self.checkforpath()
                if res == True:
                    tokens.append(self.make_path())
                else:
                    tokens.append(Token(TT_SLASH))
            elif self.current_char == '*':
                tokens.append(Token(TT_ASTERISK))
                self.advance()
            elif self.current_char == '.':
                tokens.append(Token(TT_DOT))
                self.advance()
            else:
                lexer_logger.error(f"Illegal Character '{self.current_char}' at pos: {self.pos}")
                return IllegalCharError(f"'{self.current_char}' at pos: {self.pos}")

        lexer_logger.debug(f"Finished tokenizing process for text: '{self.text}'")
        return tokens


    def make_string(self) -> Token:

        """Generates a Token of Type String."""

        string = ''

        while self.current_char != None and self.current_char in LETTERS:

            string += self.current_char
            self.advance()

        lexer_logger.debug(f"Generated TT_STR with value: '{string}'")
        return Token(TT_STR, string)


    def make_number(self) -> Token:

        """Generates Token of Type Integer."""

        num = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':

            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num += '.'
                self.advance()
            else:
                num += self.current_char
                self.advance()

        if dot_count == 0:
            lexer_logger.debug(f"Generated TT_INT with value: '{num}'")
            return Token(TT_INT, int(num))
        else:
            lexer_logger.debug(f"Generated TT_FLOAT with value: '{num}'")
            return Token(TT_FLOAT, float(num))
            

    def checkforip(self) -> bool:

        """Checks for possible IP addr"""

        iterations = 0
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':

            if self.current_char == '.':
                if dot_count == 3: break
                dot_count += 1
                iterations += 1
                self.advance()
            
            else:
                iterations += 1
                self.advance()

        if dot_count > 1:
            self.reverse(iterations)
            lexer_logger.debug("Successfully detected IP")
            return True
        else:
            self.reverse(iterations)
            lexer_logger.debug("No IP found")
            return False


    def checkforpath(self) -> bool:

        iterations = 0
        slash_count = 0

        while self.current_char != None and self.current_char in LETTERS + DIGITS + '/':

            if self.current_char == '/':
                if slash_count == 2: break
                slash_count += 1
                self.advance()
                iterations += 1
            else:
                self.advance()
                iterations += 1

        if slash_count > 1:
            self.reverse(iterations)
            lexer_logger.debug("Successfully detected path")
            return True
        else:
            self.reverse(iterations)
            lexer_logger.debug("No Path found") 
            return False 


    def make_ipaddr(self) -> Token:
        
        """Generates Token of Type IP Addr."""

        ip = ''
        dot_count = 0
        
        while self.current_char != None and self.current_char in DIGITS + '.':
            
            if self.current_char == '.':
                if dot_count == 3: break
                dot_count += 1
                ip += '.'
                self.advance()
            else:
                ip += self.current_char
                self.advance()
        
        lexer_logger.debug(f"Generated TT_IPADDR with value: '{ip}'")
        return Token(TT_IPADDR, ip)


    def make_flag(self) -> Token:
        
        """Generates Token of Type Flag."""

        flag = ''

        while self.current_char != None and self.current_char in LETTERS:

            flag += self.current_char
            self.advance()

        lexer_logger.debug(f"Created TT_FLAG with value: '{flag}'")
        return Token(TT_FlAG, flag)


    def make_path(self) -> Token:
        
        path = ''

        while self.current_char != None and self.current_char in LETTERS + DIGITS + '/':

            path += self.current_char
            self.advance()

        lexer_logger.debug(f"Created TT_PATH with value: '{path}'")
        return Token(TT_PATH, path)


####################
#Parser
####################

class Parser:

    def __init__(self, tokens: list) -> None:
        
        parser_logger.info(f"To parse: {tokens}")
        self.tokens = tokens
        self.pos = -1
        self.current_token = None
        self.advance()

    def advance(self) -> None:

        self.pos += 1

        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            parser_logger.debug(f"Advanced to pos {self.pos} with token: '{self.current_token}'")
        else:
            self.current_token = None