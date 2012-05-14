from lepl import *

class Symbol(List):
    def eval(self):
        return self[0]

class And(List):
    def eval(self):
        return self[0].eval() + "&" + self[1].eval()

class Or(List):
    def eval(self):
        return self[0].eval() + "|" + self[1].eval()

class Iff(List):
    def eval(self):
        return self[0].eval() + "<->" + self[1].eval()

class If(List):
    def eval(self):
        return self[0].eval() + "->" + self[1].eval()

class IsPredicate(List):
    def eval(self):
        return self[1].eval() + "(" + self[0].eval() + ")"

class UndefinedOp(List):
    def eval(self):
        return "x"

expression = Delayed()
symbol = ~Token('"') & Token('[a-zA-z]+') & ~Token('"') > Symbol

# operators
and_op = Token('and')
or_op = Token('or')
iff_op = Token('iff')
if_op = Token('if')
then_op = Token('then')
and_expression = symbol & ~and_op & expression > And
or_expression = symbol & ~or_op & expression > Or
iff_expression = symbol & ~iff_op & expression > Iff
if_expression = ~if_op & expression & ~then_op & expression > If


# predicates
is_op = Token('is')
undefined_op = Token("he") | Token("she") | Token("someone") > UndefinedOp
is_predicate = (symbol|undefined_op) & ~is_op & symbol > IsPredicate
predicate = is_predicate

expression += and_expression | or_expression | iff_expression | if_expression | predicate | symbol

print expression.parse('"A"')[0].eval()
print expression.parse('"A" and "B"')[0].eval()
print expression.parse('"A" or "B"')[0].eval()
print expression.parse('"A" iff "B"')[0].eval()
print expression.parse('if "A" then "B"')[0].eval()
print expression.parse('"A" or "B" and "C"')[0].eval()
print expression.parse('"A" is "B"')[0].eval()
print expression.parse('someone is "B"')[0].eval()
