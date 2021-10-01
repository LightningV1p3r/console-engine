# Copyright (c) 2021 LightningV1p3r

####################
#Libs
####################

import pytest
from src import lexer

####################
#Tokens
####################

TT_STR              = 'STR'
TT_INT              = 'INT'
TT_DOT              = 'DOT'
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

####################
#Tests
####################

class TestLexer:

    def test_TT_STR(self):
        
        val = ' teststring '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_STR, 'teststring')
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_INT(self):
        
        val = ' 1 '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_INT, 1)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_DOT(self):
        
        val = ' . '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_DOT)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_PLUS(self):
        
        val = ' + '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_PLUS)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_BANG(self):
        
        val = ' ! '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_BANG)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_FILE_1(self):
        
        val = ' file.py '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_FILE, 'file.py')
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value

    
    def test_TT_FILE_2(self):

        val = ' 1035.py '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_FILE, '1035.py')
        res = lexer_.tokenize()[0]

        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_FLAG(self):
        
        val = '-f '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_FlAG, 'f')
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_PATH(self):
        
        val = ' /example/path/ '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_PATH, '/example/path/')
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_SLASH(self):
        
        val = ' / '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_SLASH)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_FLOAT(self):
        
        val = ' 1.5 '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_FLOAT, 1.5)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_MINUS(self):
        
        val = ' - '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_MINUS)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_SHARP(self):
        
        val = ' # '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_SHARP)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_QUOTE(self):
        
        val = " ' "
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_QUOTE)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_IPADDR(self):
        
        val = ' 10.10.7.1 '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_IPADDR, '10.10.7.1')
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_ASTERISK(self):
        
        val = ' * '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_ASTERISK)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_AMPERSAND(self):
        
        val = ' & '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_AMPERSAND)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_UNDERSCORE(self):
        
        val = ' _ '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_UNDERSCORE)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value


    def test_TT_DOUBLE_QUOTE(self):
        
        val = ' " '
        lexer_ = lexer.Lexer(val)
        exp_res = lexer.Token(TT_DOUBLE_QUOTE)
        res = lexer_.tokenize()[0]
        
        assert res.type == exp_res.type
        assert res.value == exp_res.value