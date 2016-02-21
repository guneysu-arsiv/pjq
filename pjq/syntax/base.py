#!/usr/bin/env python
# coding=utf-8
import ply.lex as lex
import ply.yacc as yacc


# noinspection PyMethodMayBeStatic
class Parser(object):
    """
    Base class for a lexer/parser that has the rules defined as methods
    From: https://github.com/dabeaz/ply/blob/master/example/classcalc/calc.py
    """
    tokens = ()
    precedence = ()

    def __init__(self, **kw):
        """
        :param kw:
        :return:
        """
        self.debug = kw.get('debug', 0)
        self.names = {}
        self.output = dict()

        # Build the lexer and parser
        lex.lex(module=self, debug=self.debug)
        yacc.yacc(module=self, debug=self.debug)

    def t_error(self, t):
        t.lexer.skip(1)
        raise SyntaxError("Illegal character '%s'" % t.value[0])

    def p_error(self, p):
        if p:
            raise SyntaxError("Syntax error at '%s'" % p)
        else:
            raise EOFError("Syntax error at EOF")

    def run(self):
        while 1:
            try:
                s = raw_input('calc > ')
            except EOFError:
                break
            if not s: continue
            yacc.parse(s)
