#!/usr/bin/env python
# coding=utf-8

import ply.yacc as yacc

import base

# region Description
__data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}


# endregion

# noinspection PyPep8Naming,PyMethodMayBeStatic,PyIncorrectDocstring,PySingleQuotedDocstring
class Lexer(base.Parser):
    """
    1. Top level types
        - Array
        - Dictionary

     Top level object should be a dictionary. I am working on also accepting array as a top level data.

    2. Sub level types
        - Array
        - Dictionary
        - Primitive types

    # Selecting properties
        Dividing works by forward slash `/`.
        At least one property must be given. There is not `*` or `.` that select all properties.

    ```
    store
    store/book
    store/book/category
    ```

    # Selecting multiple properties
    Use comma `,` and wrap with parantheses `()` for giving multiple property.
    By selecting multiple properties, properties would be sorted by alphabetically. Not the order of given.
    But this is my choice. This may be change.
    ```
    store/(book,bicyle)
    ```
    Only first level grouping is being implemented/planned. Complex queries are not implemented.

    Like
    ```
    store/(book/category, bicyle)
    ```

    # Slicing Arrays
    Slicing array properties works like numpy/matlab syntax.
    1. Single index
    2. Index range
    3. Multiple Index

    1. Single index
    ```
    store/book[0]
    ```

    2. Index range
    ```
    store/book[1:3] # Selects obj["store"]["book"][1] and obj["store"]["book"][2]
    ```
    3. Multiple Index
    Seperate multiple indexes with comma `,`
    ```
    store/book[0,2]
    ```
    """

    def __init__(self, data, **kw):
        # region Documentation
        """
        Lexer class (for now) must be instantiated with dictionary/list/tuple data.
        Since date extracting is made while lexing process.
        I am working on extracting complex data by seperating lexing process.

        >>> import ply.yacc as yacc
        >>> from pjq.syntax.lexer import Lexer
        >>> data = dict(\
            name="Tech Class",  \
            classroom=dict(name="DBA", ids=["0 (-3)", "1 (-2)", "2 (-1)"]) \
        )
        >>> _ = Lexer(data=data)
        >>> print yacc.parse("classroom")
        {'ids': ['0 (-3)', '1 (-2)', '2 (-1)'], 'name': 'DBA'}

        >>> print yacc.parse("name")
        Tech Class
        >>> _  = Lexer(data=data["classroom"])
        >>> print yacc.parse("ids")
        ['0 (-3)', '1 (-2)', '2 (-1)']

        >>> _ = Lexer(data=data["classroom"]["ids"])

        >>> print yacc.parse("[]")
        ['0 (-3)', '1 (-2)', '2 (-1)']

        >>> print yacc.parse("[:]")
        ['0 (-3)', '1 (-2)', '2 (-1)']

        >>> print yacc.parse("[0]")
        0 (-3)

        >>> print yacc.parse("[-1]")
        2 (-1)

        >>> print yacc.parse("[-1:1]")
        ['2 (-1)', '0 (-3)']

        >>> print yacc.parse("[2,0]")
        ['2 (-1)', '0 (-3)']

        >>> print yacc.parse("[-1:1]")
        ['2 (-1)', '0 (-3)']

        >>> print yacc.parse("[-1:3]")
        ['2 (-1)', '0 (-3)', '1 (-2)', '2 (-1)']

        :type data: object
        :param data:
        :param kw:
        :return:
        """
        # endregion
        self.data = data
        super(Lexer, self).__init__(**kw)

    tokens = (
        "PROPERTY",
        "LBRACKET",
        "RBRACKET",
        "NUMBER",
    )

    literals = [':', ',']

    # Tokens
    t_PROPERTY = r"[a-zA-Z_][a-zA-Z0-9_]*"
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_ignore = " \t"

    def t_NUMBER(self, t):
        r'-?[0-9]+'
        # r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %s" % t.value)
            raise
        return t

    def p_number(self, p):
        'expression : NUMBER'
        p[0] = p[1]

    def p_array_property(self, p):
        '''expression : LBRACKET RBRACKET
                      | LBRACKET ':' RBRACKET
        '''
        p[0] = self.data[:]

    def p_array_property_single(self, p):
        '''expression : LBRACKET NUMBER RBRACKET
        '''
        p[0] = self.data[p[2]]

    def p_array_property_range(self, p):
        '''expression : LBRACKET NUMBER ':' NUMBER RBRACKET
        '''
        p[0] = [self.data[i] for i in range(p[2], p[4])]

    def p_array_property_double(self, p):
        '''expression : LBRACKET NUMBER ',' NUMBER RBRACKET
        '''
        p[0] = [self.data[i] for i in [p[2], p[4]]]

    def p_property(self, p):
        'expression : PROPERTY'
        p[0] = self.data[p[1]]

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")


# noinspection PyUnresolvedReferences,PyUnusedLocal
def main():
    c = Lexer(debug=True, data=__data["store"])
    # c.run()
    # print yacc.parse("-100")
    print yacc.parse("bicycle")
    # print yacc.parse("book[]")
    # print yacc.parse("book[:]")
    # print yacc.parse("book[0]")
    # print yacc.parse("book[2:4]")
    # print c.output


if __name__ == '__main__':
    main()
