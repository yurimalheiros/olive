from lepl import List

class Symbol(List):
    """
    A symbol value. It is represented by "aName".
    """
    def eval(self):
        return self[0]

class Undefined(List):
    """
    A undefined value. It is represented by he, she or someone.
    """
    def eval(self):
        return "x"

