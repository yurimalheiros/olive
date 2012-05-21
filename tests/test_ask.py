import oliveask
from olive import grammar
from olive import knowledgebase

def test_save_expression():
    knowledgebase.clear()
    oliveask.eval('"A"')
    oliveask.eval('"A" or "B"')
    assert [str(x) for x in knowledgebase.get_all()] == ["A", "(A | B)"]

def test_question_eval():
    knowledgebase.clear()
    oliveask.eval('"A"')
    assert grammar.expression.parse('question:"A"?')[0].eval() == True
    assert grammar.expression.parse('question:"B"?')[0].eval() == False

def test_socrates_question():
    oliveask.eval('"Socrates" is "human"')
    oliveask.eval('if someone is "human" then he is "intelligent"')
    assert grammar.expression.parse('question:"Socrates" is "intelligent"?')[0].eval() == True


