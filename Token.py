
TOKEN_TYPE = ('HJ', 'ACC', 'FRP', 'NUM', 'STR')

class Token:

    def  __init__(self, string):
        self.type = None
        self.value = None
        self.recognize(string)

    def recognize(self, string):
        for i in range(3):
            if TOKEN_TYPE[i] == string:
                self.type = i
                return
        try:
            self.value = float(string)
            self.type = 3
            return
        except ValueError:
            pass

        self.value = string
        self.type = 4

    def __str__(self):
        return TOKEN_TYPE[self.type]+ " " + self.value
