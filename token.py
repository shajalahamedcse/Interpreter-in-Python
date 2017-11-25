# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis


class Token(object):
    def __init__(self,type,value):
        # token type: INTEGER, PLUS, or EOF
        self.type=type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value=value

    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type,value=repr(self.value) )

    def __repr__(self):
        return self.__str__()