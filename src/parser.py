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

class CommandNode:

    def __init__(self, keyword, args) -> None:
        self.keyword = keyword
        self.args = args


class ArgumentNode:

    def __init__(self, flag, args) -> None:

        self.flag = flag
        self.args = args


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

        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            parser_logger.debug(f"Advanced to pos {self.pos} with token: '{self.current_token}'")
        else:
            self.current_token = None