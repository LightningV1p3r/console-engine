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

class ExpressionNode:
    
    def __init__(self, node1) -> None:
        self.node1 = node1

    def as_string(self) -> str:
        res = f'({self.node1})'
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        print(self.as_string())


class TermNode:

    def __init__(self, node1, node2) -> None:
        self.node1 = node1
        self.node2 = node2

    def as_string(self) -> str:
        res = f'({self.node1} + {self.node2})'
        return res 

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        print(self.as_string())

    
class FlagNode:

    def __init__(self, val) -> None:
        self.val = val

    def as_string(self) -> str:
        res = f"'FLAG: {self.val}'"
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        print(self.as_string())


class KeywordNode:

    def __init__(self, val) -> None:
        self.val = val

    def as_string(self) -> str:
        res = f"'KEYWORD: {self.val}'"
        return res
    
    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        print(self.as_string())

class ArgNode:

    def __init__(self, type, val) -> None:
        self.type = type
        self.val = val

    def as_string(self) -> str:
        res = f"'{self.type}: {self.val}'"
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        print(self.as_string())

####################
#Parser
####################

class Parser:

    def __init__(self) -> None:
        pass