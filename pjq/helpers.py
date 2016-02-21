#!/usr/bin/env python
# coding=utf-8
import ply.yacc as yacc
import syntax.lexer


def query(obj, selector):
    lexer = syntax.lexer.Lexer(debug=False, data=obj)

    extracted = yacc.parse(selector)
    return extracted
