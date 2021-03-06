import oliveask
from olive import grammar
from olive import knowledgebase

def test_save_expression():
    knowledgebase.clear()
    oliveask.eval('A.')
    oliveask.eval('A or B.')
    assert [str(x) for x in knowledgebase.get_all()] == ["A", "(A | B)"]

def test_question_eval():
    knowledgebase.clear()
    oliveask.eval('A.')
    assert grammar.program.parse('A?')[0].eval() == True
    assert grammar.program.parse('B?')[0].eval() == False

def test_socrates_question():
    oliveask.eval('Socrates is Human.')
    oliveask.eval('if someone is Human then he is Intelligent.')
    assert grammar.program.parse('Socrates is Intelligent?')[0].eval() == True


