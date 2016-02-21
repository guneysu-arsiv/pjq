#!/usr/bin/env python
# coding=utf-8
"""
Lexer class must be insta
"""
import unittest
import ply.yacc as yacc
from pjq.syntax.lexer import Lexer
class LexerTest(unittest.TestCase):
    @unittest.skip("Example Test")
    def test_1(self):
        assert True


if __name__ == '__main__':
    Lexer(debug=True)
    print yacc.parse("bicycle")
