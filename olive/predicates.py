from lepl import List

class Is(List):
    """
    Is predicate. It is represented by: $value is $symbol.
    """
    def eval(self):
        return self[1] + "(" + self[0].eval() + ")"

class Misc(List):
    """
    Varied types of predicates. It is represented by: $value any words $symbol.
    """
    def eval(self):
        if len(self) == 2:
            return self[1] + "(" + self[0].eval() + ")"
        elif len(self) > 2:
            return '_'.join(self[1:-1]) + "(" + self[0].eval() + "," + self[-1].eval() + ")"
