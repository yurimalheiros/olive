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

expression = Delayed()
symbol = ~Token('"') & Token('[a-zA-z]+') & ~Token('"') > Symbol
and_op = Token('and')
or_op = Token('or')
and_expression = symbol & ~and_op & expression > And
or_expression = symbol & ~or_op & expression > Or
expression += and_expression | or_expression | symbol

print expression.parse('"A"')[0].eval()
print expression.parse('"A" and "B"')[0].eval()
print expression.parse('"A" or "B"')[0].eval()
print expression.parse('"A" or "B" and "C"')[0].eval()
