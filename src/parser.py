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
    
    def __init__(self, node1, node2=None) -> None:
        self.node1 = node1
        self.node2 = node2

    def as_string(self) -> str:
        
        if self.node2 == None:
            res = f'({self.node1})'
            return res
        else:
            res = f'({self.node1} + {self.node2})'
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

    ####################
    #Checker
    ####################


        
    ####################
    #parsing
    ####################

    def parse(self):
        return self.expression()

    def expression(self):
        pass

    def command(self):
        pass

    def keyword(self):
        pass

    def keyword_chain(self):
        pass

    def flag(self):
        pass

    def value(self):
        pass

    def flag_value_pair(self):
        pass

    def data_chain(self):
        pass
