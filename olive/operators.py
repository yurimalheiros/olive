from lepl import List

class And(List):
    """
    And logic operator.
    """
    def eval(self):
        return self[0].eval() + "&" + self[1].eval()

class Or(List):
    """
    Or logic operator.
    """
    def eval(self):
        return self[0].eval() + "|" + self[1].eval()

class Iff(List):
    """
    Iff logic operator.
    """
    def eval(self):
        return self[0].eval() + "<->" + self[1].eval()

class If(List):
    """
    If-then logic operator.
    """
    def eval(self):
        return self[0].eval() + "->" + self[1].eval()

