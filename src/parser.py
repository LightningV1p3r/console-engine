# Copyright (c) 2021 LightningV1p3r

####################
# Libs
####################

import viperlogger
from dataclasses import dataclass

####################
# Logger
####################

parser_logger = viperlogger.Logger("Parser")

####################
#Nodes
####################

@dataclass
class ExpressionNode:
    expr = tuple


@dataclass
class CommandNode:
    keyword = None
    args = tuple


@dataclass
class KeywordNode:
    value = str


@dataclass
class ArgumentNode:
    flag = None
    value = None
 

@dataclass
class FlagNode:
    value = str


@dataclass
class ValueNode:
    value = None


####################
# Parser
####################

class Parser:

    def __init__(self, tokens: list, args: list) -> None:
        
        parser_logger.info(f"To parse: {tokens}")
        self.tokens = tokens
        self.pos = -1
        self.current_token = None
        self.advance()

    def advance(self) -> None:

        self.pos += 1

        if self.current_token.type == 'EOF':
            self.current_token = None
        else:
            self.current_token = self.tokens[self.pos]
            parser_logger.debug(f"Advanced to pos {self.pos} with token: '{self.current_token}'")
        
    def parse(self):

        if self.current_token == None:
            return None

        result = self.expr()

        return result

    def expr(self):
        pass

    def cmd(self):
        pass

    def arg(self):
        pass

    def flag(self):
        pass

    def val(self):
        pass