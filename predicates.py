#Predicates (example 1 and 2)

class Knows(object):

        def __init__(self, x, info):
                self.x = x
                self.info = info

        def listar(self):
                if (type(self.info) is Key) or (type(self.info) is Encoded) :
                        return ['knows', self.x, self.info.listar()]
                else:
                        return ['knows', self.x, self.info]

class Key(object):

        def __init__(self, x1, x2):
                self.x1 = x1
                self.x2 = x2

        def listar(self):
                return ['key', self.x1, self.x2]

class Dec(object):

        def __init__(self, x, Encoded):
                self.x = x
                self.enc = Encoded

        def listar(self):
                return ['decode', self.x, self.enc.listar()]

class Sent(object):

        def __init__(self, Encoded, x1, x2):
                self.enc = Encoded
                self.x1 = x1
                self.x2 = x2

        def listar(self):
                return ['sent', self.enc.listar(), self.x1, self.x2]

class Received(object):

        def __init__(self, Encoded, x2, x1):
                self.enc = Encoded
                self.x2 = x2
                self.x1 = x1

        def listar(self):
                return ['received', self.enc.listar(), self.x1, self.x2]

class Intercepted(object):

        def __init__(self, x3, Encoded, x1, x2):
                self.x3 = x3
                self.enc = Encoded
                self.x1 = x1
                self.x2 = x2

        def listar(self):
                return ['intercepted', self.x3, self.enc.listar(), self.x1, self.x2]

#Predicates of example 1
class Encoded(object):

        def __init__(self, message, Key):
                self.message = message
                self.key = Key

        def listar(self):
                return ['encoded', self.message, self.key.listar()]

class Enc(object):

        def __init__(self, x, message, Key):
                self.x = x
                self.message = message
                self.key = Key

        def listar(self):
                return ['encode', self.x, self.message, self.key.listar()]

#Predicates of example 2

class Concat(object):

    def __init__(self, message, Key):
        self.message = message
        self.key = Key

    def listar(self):
        return ['concat', self.message, self.key.listar()]

class Conc(object):

    def __init__(self, x, message, Key):
        self.x = x
        self.message = message
        self.key = Key

    def listar(self):
        return ['concatenate', self.x, self.message, self.key.listar()]

class Deconc(object):

    def __init__(self, x, Concat):
        self.x = x
        self.concat = Concat

    def listar(self):
        return ['deconcat', self.x, self.concat.listar()]

class Encoded2(object):

    def __init__(self, Concat, Key):
            self.concat = Concat
            self.key = Key

    def listar(self):
            return ['encoded', self.concat.listar(), self.key.listar()]

class Enc2(object):

    def __init__(self, x, Concat, Key):
            self.x = x
            self.concat = Concat
            self.key = Key

    def listar(self):
            return ['enc', self.x, self.concat.listar(), self.key.listar()]
