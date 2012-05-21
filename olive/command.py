from lepl import List
from olive import knowledgebase

class Question(List):
    """
    A question command. It is represented by "aName".
    """
    def eval(self):
        return knowledgebase.ask(self[0].eval())
        
