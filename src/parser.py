# Copyright (c) 2021 LightningV1p3r

####################
# Libs
####################

import viperlogger

####################
# Logger
####################

parser_logger = viperlogger.Logger("Parser")

####################
#Nodes
####################

    ####################
    #Non Terminals
    ####################

class ExpressionNode:

    def __init__(self, list) -> None:
        self.list = list

    def as_string(self) -> str:
        
        res = '('
        iterations = 0

        for i in self.list:
            res += str(i)
            iterations += 1

            if iterations < len(self.list):
                res += ' + '
        
        res += ')'

        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()

class CommandNode:

    def __init__(self, node1, node2) -> None:
        self.node1 = node1
        self.node2 = node2

    def as_string(self) -> str:
        
        res = f'({self.node1} + {self.node2})'
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()


class FlagValueNode:

    def __init__(self, node1, node2) -> None:
        self.node1 = node1
        self.node2 = node2

    def as_string(self) -> str:
        
        res = f'({self.node1} + {self.node2})'
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()


class KeywordChainNode:

    def __init__(self, list) -> None:
        self.list = list

    def as_string(self) -> str:
        
        res = '('
        iterations = 0

        for i in self.list:
            res += str(i)
            iterations += 1

            if iterations < len(self.list):
                res += ' + '
        
        res += ')'

        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()


class DataChainNode:

    def __init__(self, list) -> None:
        self.list = list

    def as_string(self) -> str:
        
        res = '('
        iterations = 0

        for i in self.list:
            res += str(i)
            iterations += 1

            if iterations < len(self.list):
                res += ' + '
        
        res += ')'

        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()

class FlagChainNode:

    def __init__(self, list) -> None:
        self.list = list

    def as_string(self) -> str:
        
        res = '('
        iterations = 0

        for i in self.list:
            res += str(i)
            iterations += 1

            if iterations < len(self.list):
                res += ' + '
        
        res += ')'

        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()
 
    ####################
    #Terminals
    ####################

class KeywordNode:

    def __init__(self, value) -> None:
        self.value = value

    def as_string(self) -> str:
        
        res = f'({self.value})'
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()


class FlagNode:

    def __init__(self, value) -> None:
        self.value = value

    def as_string(self) -> str:
        
        res = f'({self.value})'
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()


class ValueNode:

    def __init__(self, value) -> None:
        self.value = value

    def as_string(self) -> str:
        
        res = f'({self.value})'
        return res
    
    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()

####################
#Parser
####################

class Parser:

    def __init__(self, tokens, keywords) -> None:
        self.tokens = tokens
        self.keywords = keywords
        self.pos = -1
        self.current_token = None
        self.advance()

    def advance(self) -> None:
        
        self.pos += 1

        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            parser_logger.debug(f"Advanced to token '{self.current_token}' at pos {self.pos}")
        
        else:
            self.current_token = None

        print('a - ' + str(self.current_token))

    def reverse(self, iterations=1):

        iter_count = 0

        while iter_count < iterations:

            self.pos -= 1

            if self.pos < 0:
                self.pos += 1
                parser_logger.error('Failed to reverse pos due to invalid index!')
            else:
                self.current_token = self.tokens[self.pos]
                parser_logger.debug(f"Reversed to pos {self.pos} with value: '{self.current_token}'")

            iter_count += 1

        print('r - ' + str(self.current_token))
    ####################
    #Checker
    ####################

    def check_for_kc(self):

        iterations = 0
        keyword_count = 0

        while self.current_token.value in self.keywords:
            
            if self.current_token.value in self.keywords:
                keyword_count += 1
            iterations += 1
            self.advance()

        self.reverse(iterations)

        if keyword_count > 1:

            return True
        else: 
            return False

    def check_for_fvp(self):
        print('check_fvp')

        if self.current_token != None:
            if self.current_token.type != 'EOF':
        
                if self.current_token.type == 'FLAG':
                    self.advance()

                    if self.current_token.type != 'FLAG' and self.current_token.type != 'EOF':
                        self.reverse()
                        return True
                    else:
                        self.reverse()
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def check_for_dc_complex(self):
        print('check dc_c')
        flag_chain = False
        fvp = False

        flags = 0
        iterations = 0

        while self.current_token.type == 'FLAG':
            flags += 1
            iterations += 1
            self.advance()

        self.reverse()

        if self.check_for_fvp() == True:
            fvp = True

        self.reverse(iterations -1)

        if flags >= 2 and fvp == True:
            flag_chain = True

        if flag_chain == True and fvp == True:

            return True, flags - 1
        else:

            return False, None

    def check_for_dc_simple(self):
        print("check dc_s")
        iterations = 0

        if self.check_for_fvp() == True:
            self.advance()
            self.advance()
            iterations += 2
            if self.check_for_fvp() == True:
                self.reverse(iterations)
                print("res - true")
                return True
            else:
                self.reverse(iterations)
                print('res - f')
                return False
        else:
            print('res - f')
            return False

    def check_for_fc(self):
        
        iterations = 0
        flag_count = 0

        while self.current_token.type == 'FLAG':
            flag_count += 1
            iterations += 1
            self.advance()
        
        self.reverse(iterations)

        if flag_count > 1:
            return True, flag_count
        else:
            return False

    ####################
    #parsing
    ####################

    def parse(self):
        return self.expression()


    def expression(self):

        res = []

        if self.current_token != None:
        
            res.append(self.command())
            self.advance()

            while True:
                if self.current_token == None or self.current_token.type == 'EOF':
                    break

                if self.current_token.type == 'AMPERSAND':
                    self.advance()
                    if self.current_token.type == 'AMPERSAND':
                        self.advance()
                        res.append(self.command())
                    else:
                        res.append(self.command())

                self.advance()

            return ExpressionNode(res)

    def command(self):

        if self.current_token.value in self.keywords:
            left = self.keyword()
        else:
            return None
        
        self.advance()
            
        if self.current_token.type == 'FLAG':

            check_dc_c, flag_count = self.check_for_dc_complex()

            if check_dc_c == True:
                right = self.data_chain("complex", flag_count)
            
            elif self.check_for_dc_simple() == True:
                right = self.data_chain("simple")

            elif self.check_for_fvp() == True:
                right = self.flag_value_pair()
            
            elif self.check_for_fc() == True:
                right = self.flag_chain()    

            else:
                right = self.flag()

        else:
            right = self.value()

        return CommandNode(left, right)

    def keyword(self):

        if self.current_token.value in self.keywords:
            if self.check_for_kc() == True:
                return self.keyword_chain()
            else:
                return KeywordNode(self.current_token.value)
        else:
            return None

    def keyword_chain(self):

        res = []
        
        while self.current_token.value in self.keywords:
            res.append(self.current_token.value)
            self.advance()

        self.reverse()
        return KeywordChainNode(res)

    def flag(self):
        print('F')
        return FlagNode(self.current_token.value)

    def value(self):
        return ValueNode(self.current_token)

    def flag_value_pair(self):
        print("fvp")
        flag = self.flag()
        self.advance()
        value = self.value()
        return FlagValueNode(flag, value)

    def data_chain(self, mode, flag_count=None):
        print("dc")
        res = []

        if mode == 'complex':
            res.append(self.flag_chain('counter',flag_count))
        while True:
            if self.check_for_fvp() == True:
                res.append(self.flag_value_pair())
                self.advance()
            else:
                break
        return DataChainNode(res)

    def flag_chain(self, mode, flag_count):
        print(f'fc - {flag_count}')
        res = []
        iterations = 0
        if mode == 'counter':
            while iterations < flag_count:
                iterations += 1
                res.append(self.flag())
                self.advance()
        else:
            while self.current_token.type == 'FLAG':
                res.append(self.flag())
                self.advance()

        return FlagChainNode(res)
