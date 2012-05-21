import nltk

lp = nltk.LogicParser()
prover = nltk.Prover9()
kb = []

def add(data):
    kb.append(lp.parse(data))

def get_all():
    return kb

def clear():
    global kb
    kb = []

def ask(data):
    return prover.prove(lp.parse(data), kb)
