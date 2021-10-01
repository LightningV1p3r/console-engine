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

####################
#Constants
####################

LETTERS     = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS      = '0123456789'

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

TT_STR              = 'STR'
TT_INT              = 'INT'
TT_DOT              = 'DOT'
TT_EOF              = 'EOF'
TT_PLUS             = 'PLUS'
TT_BANG             = 'BANG'
TT_FILE             = 'FILE'
TT_FlAG             = 'FLAG'
TT_PATH             = 'PATH'
TT_SLASH            = 'SLASH'
TT_FLOAT            = 'FLOAT'
TT_MINUS            = 'MINUS'
TT_SHARP            = 'SHARP'
TT_QUOTE            = 'QUOTE'
TT_IPADDR           = 'IPADDR'
TT_ASTERISK         = 'ASTERISK'
TT_AMPERSAND        = 'AMPERSAND'
TT_UNDERSCORE       = 'UNDERSCORE'
TT_DOUBLE_QUOTE     = 'DOUBLE_QUOTE'
TT_FILE_EXTENSION   = 'FILE_EXTENSION'

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
        
        lexer_logger.debug("============================== Tokenizing START ==============================")
        lexer_logger.debug(f"To tokenize: '{text}'")
        self.text = text
        self.pos = -1
        self.current_char = None
        self.tokens = []
        self.advance()

    ####################
    #Assets
    ####################

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


    def merge_tokens(self, tok1: Token, tok2: Token, res_tok_type: Token) -> Token:
        
        val1 = tok1.value
        val2 = tok2.value

        if val1 == int() or float() and val2 == int() or float():
            res_value = val1 + val2
        else:
            res_value = str(val1) + str(val2)

        lexer_logger.debug(f"Merged Tokens '{tok1}', '{tok2}' to Token with value: '{res_value}'")
        return Token(res_tok_type, res_value)


    def tokenize(self) -> list:
        
        """Start the process of tokenizing."""

        while self.current_char != None:
            
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in LETTERS:
                self.tokens.append(self.make_string())
            elif self.current_char in DIGITS:
                self.tokens.append(self.handle_digit())
            elif self.current_char == '-':
                self.tokens.append(self.handle_minus())
            elif self.current_char == '+':
                self.tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '/':
                self.tokens.append(self.handle_slash())
            elif self.current_char == '*':
                self.tokens.append(Token(TT_ASTERISK))
                self.advance()
            elif self.current_char == '.':
                self.tokens.append(self.handle_dot())
            elif self.current_char == '!':
                self.tokens.append(Token(TT_BANG))
                self.advance()
            elif self.current_char == '#':
                self.tokens.append(Token(TT_SHARP))
                self.advance()
            elif self.current_char == "'":
                self.tokens.append(Token(TT_QUOTE))
                self.advance()
            elif self.current_char == '&':
                self.tokens.append(Token(TT_AMPERSAND))
                self.advance()
            elif self.current_char == '_':
                self.tokens.append(Token(TT_UNDERSCORE))
                self.advance()
            elif self.current_char == '"':
                self.tokens.append(Token(TT_DOUBLE_QUOTE))
                self.advance()
            else:
                lexer_logger.error(f"Illegal Character '{self.current_char}' at pos: {self.pos}")
                return IllegalCharError(f"'{self.current_char}' at pos: {self.pos}")

        self.tokens.append(Token(TT_EOF))

        lexer_logger.debug(f"Finished tokenizing process for text: '{self.text}'")
        lexer_logger.debug("============================== Tokenizing END ==============================\n")
        
        return self.tokens
            
    
    ####################
    #Checker
    ####################


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

        """Checks for pssible Path."""

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


    def checkforfile(self) -> bool:
        
        iterations = -1
        file_found = bool()

        while self.current_char != None and self.current_char in LETTERS + DIGITS + '.':

            if self.current_char in ' \t':
                break
            
            elif self.current_char in DIGITS:
                file_found = False
                break
            else: 
                file_found = True

            self.advance()
            iterations += 1
        
        if file_found == False:
            self.reverse(iterations + 1)
            lexer_logger.debug("No file found")
            return False
        elif iterations >= 1:
            self.reverse(iterations + 1)
            lexer_logger.debug("File found")
            return True
        else:
            self.reverse(iterations + 1)
            lexer_logger.debug("No file found")
            return False


    ####################
    #handlers
    ####################

    def handle_digit(self) -> Token:
        
        res = self.checkforip()
        
        if res == True:
            return self.make_ipaddr()
        else:
            return self.make_number()


    def handle_minus(self) -> Token:
        
        self.advance(2)
        if self.current_char != None and self.current_char in ' \t':
            self.reverse()
            return self.make_flag()
        else:
            self.reverse(2)
            self.advance()
            return Token(TT_MINUS)


    def handle_slash(self) -> Token:

        res = self.checkforpath()
        if res == True:
            return self.make_path()
        else:
            self.advance()
            return Token(TT_SLASH)


    def handle_dot(self):
        
        res = self.checkforfile()
        if res == True:
            self.tokens.append(self.make_file_extension())
            return self.make_file()
        else:
            self.advance()
            return Token(TT_DOT)


    ####################
    #Token generators
    ####################

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
        is_file = False

        while self.current_char != None and self.current_char in DIGITS + '.':

            if self.current_char == '.':
                if dot_count == 1: break
                file_res = self.checkforfile()
                    
                if file_res == False:
                    dot_count += 1
                    num += '.'
                    self.advance()
                else:
                    is_file = True
                    break
                    
            else:
                num += self.current_char
                self.advance()
        if is_file == True:
            self.tokens.append(Token(TT_INT, int(num)))
            self.tokens.append(self.make_file_extension())
            return self.make_file()
        elif dot_count == 0:
            lexer_logger.debug(f"Generated TT_INT with value: '{num}'")
            return Token(TT_INT, int(num))
        else:
            lexer_logger.debug(f"Generated TT_FLOAT with value: '{num}'")
            return Token(TT_FLOAT, float(num))


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

            if self.current_char in ' \t': break

            flag += self.current_char
            self.advance()

        lexer_logger.debug(f"Created TT_FLAG with value: '{flag}'")
        return Token(TT_FlAG, flag)


    def make_path(self) -> Token:

        """Generates Token of Type Path."""
        
        path = ''

        while self.current_char != None and self.current_char in LETTERS + DIGITS + '/':

            path += self.current_char
            self.advance()

            if self.current_char == '.':
                
                iterations = 0

                while True:
                    
                    if self.current_char == '/': 
                        iterations -= 1
                        self.advance() 
                        break
                    
                    self.reverse()
                    iterations += 1
                
                path = path[:-iterations]
                break

        lexer_logger.debug(f"Created TT_PATH with value: '{path}'")
        return Token(TT_PATH, path)


    def make_file(self) -> Token:

        try:
            filename = self.tokens[-2]
            file_ext = self.tokens[-1]
        except IndexError:
            filename = self.tokens[1]
            file_ext = self.tokens[2]

        file_ = self.merge_tokens(filename, file_ext, TT_FILE)

        try:
            del self.tokens[-1]
            del self.tokens[-1]
        except IndexError:
            del self.tokens[-1]

        lexer_logger.debug(f"Created TT_FILE with value: '{file_.value}'")
        return file_


    def make_file_extension(self) -> Token:
        
        file_extension = ''

        while self.current_char != None and self.current_char in LETTERS + DIGITS + '.':

            if self.current_char in ' \t':
                break

            file_extension += self.current_char
            self.advance()

        lexer_logger.debug(f"Created TT_FILE_EXTENSION with value: '{file_extension}'")
        return Token(TT_FILE_EXTENSION, file_extension)