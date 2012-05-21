from olive import grammar

def test_symbol():
    assert grammar.expression.parse('"A"')[0].eval() == "A"

def test_and_op():
    assert grammar.expression.parse('"A" and "B"')[0].eval() == "A&B"

def test_or_op():
    assert grammar.expression.parse('"A" or "B"')[0].eval() == "A|B"

def test_iff_op():
    assert grammar.expression.parse('"A" iff "B"')[0].eval() == "A<->B"

def test_if_op():
    assert grammar.expression.parse('if "A" then "B"')[0].eval() == "A->B"

def test_or_and_op():
    assert grammar.expression.parse('"A" or "B" and "C"')[0].eval() == "A|B&C"

def test_is_predicate():
    assert grammar.expression.parse('"A" is "B"')[0].eval() == "B(A)"

def test_is_predicate_undefined_op():
    assert grammar.expression.parse('someone is "B"')[0].eval() == "B(x)"

def test_misc_predicate_transitive():
    assert grammar.expression.parse('"A" bring "B"')[0].eval() == "bring(A,B)"

def test_misc_predicate_intransitive():
    assert grammar.expression.parse('"A" gone')[0].eval() == "gone(A)"
