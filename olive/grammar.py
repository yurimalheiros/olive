from lepl import *
import values
import operators
import predicates
import command

words_with_space = Delayed()
expression = Delayed()
program = Delayed()

# values
#symbol = ~Token('"') & Token('[a-zA-Z]+') & ~Token('"') > values.Symbol
symbol = Token('[A-Z][a-zA-Z]*') > values.Symbol
word = Token('[a-z]+')
words_with_space = word & Star(word)
undefined_op = Token("he") | Token("she") | Token("someone") > values.Undefined

# operators
and_op = Token('and')
or_op = Token('or')
iff_op = Token('iff')
if_op = Token('if')
then_op = Token('then')
and_expression = symbol & ~and_op & expression > operators.And
or_expression = symbol & ~or_op & expression > operators.Or
iff_expression = symbol & ~iff_op & expression > operators.Iff
if_expression = ~if_op & expression & ~then_op & expression > operators.If

# predicates
is_op = Token('is')
is_predicate = (symbol|undefined_op) & ~is_op & symbol > predicates.Is
misc_predicate = (symbol|undefined_op) & words_with_space & Optional(symbol) > predicates.Misc
predicate = is_predicate | misc_predicate

# command
questionmark_op = Token('\\?')
question = expression & ~questionmark_op > command.Question
premise = expression & ~Token('\\.') > command.Premise

expression += and_expression | or_expression | iff_expression | if_expression | predicate | symbol
program += premise | question
