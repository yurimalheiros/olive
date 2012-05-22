from olive import grammar

def test_symbol():
    assert grammar.program.parse('A.')[0].eval() == "A"

def test_and_op():
    assert grammar.program.parse('A and B.')[0].eval() == "A&B"

def test_or_op():
    assert grammar.program.parse('A or B.')[0].eval() == "A|B"

def test_iff_op():
    assert grammar.program.parse('A iff B.')[0].eval() == "A<->B"

def test_if_op():
    assert grammar.program.parse('if A then B.')[0].eval() == "A->B"

def test_or_and_op():
    assert grammar.program.parse('A or B and C.')[0].eval() == "A|B&C"

def test_is_predicate():
    assert grammar.program.parse('A is B.')[0].eval() == "B(A)"

def test_is_predicate_undefined_op():
    assert grammar.program.parse('someone is B.')[0].eval() == "B(x)"

def test_misc_predicate_transitive():
    assert grammar.program.parse('A bring B.')[0].eval() == "bring(A,B)"
    assert grammar.program.parse('A go by B.')[0].eval() == "go_by(A,B)"

def test_misc_predicate_intransitive():
    assert grammar.program.parse('A gone.')[0].eval() == "gone(A)"
