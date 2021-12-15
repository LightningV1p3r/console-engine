# Copyright (c) 2021 LightningV1p3r

####################
#Libs
####################

import pytest
from src import parser, lexer

####################
#TestInputs
####################

C_KV = 'kywrd 10'
C_KDC_C = 'kywrd -f -t -i 10.10.7.10'
C_KDC_S = 'kywrd -f flag -v value'
C_KF = 'kywrd -f'
C_KFVP = 'kywrd -f 10'
C_KCV = 'kywrd do file.py'
C_KCDC_C = 'kywrd do -f -t -i 10.10.7.10'
C_KCDC_S = 'kywrd do -f flag -v value'
C_KCF = 'kywrd do -t'
C_KCFVP = 'kywrd do -t 10.10.7.10'

####################
#Constants
####################

KEYWORDS = ['kywrd', 'do']

####################
#Tests
####################

class TestParser:

    def test_C_KV(self):
        
        exp_res_str = '(((kywrd) + (INT: 10)))'

        lexer_ = lexer.Lexer(C_KV)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KDC_C(self):
        
        exp_res_str = '(((kywrd) + (((f) + (t)) + ((i) + (IPADDR: 10.10.7.10)))))'

        lexer_ = lexer.Lexer(C_KDC_C)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KDC_S(self):
        
        exp_res_str = '(((kywrd) + (((f) + (STR: flag)) + ((v) + (STR: value)))))'

        lexer_ = lexer.Lexer(C_KDC_S)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KF(self):
        
        exp_res_str = '(((kywrd) + (f)))'

        lexer_ = lexer.Lexer(C_KF)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KFVP(self):
        
        exp_res_str = '(((kywrd) + ((f) + (INT: 10))))'

        lexer_ = lexer.Lexer(C_KFVP)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KCV(self):
        
        exp_res_str = '(((kywrd + do) + (FILE: file.py)))'

        lexer_ = lexer.Lexer(C_KCV)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KCDC_C(self):
        
        exp_res_str = '(((kywrd + do) + (((f) + (t)) + ((i) + (IPADDR: 10.10.7.10)))))'

        lexer_ = lexer.Lexer(C_KCDC_C)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KCDC_S(self):
        
        exp_res_str = '(((kywrd + do) + (((f) + (STR: flag)) + ((v) + (STR: value)))))'

        lexer_ = lexer.Lexer(C_KCDC_S)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KCF(self):
        
        exp_res_str = '(((kywrd + do) + (t)))'

        lexer_ = lexer.Lexer(C_KCF)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)

    def test_C_KCFVP(self):
        
        exp_res_str = '(((kywrd + do) + ((t) + (IPADDR: 10.10.7.10))))'

        lexer_ = lexer.Lexer(C_KCFVP)
        lex_res = lexer_.tokenize()

        parser_ = parser.Parser(lex_res, KEYWORDS)
        parse_res = parser_.parse()

        assert exp_res_str == str(parse_res)