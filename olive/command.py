from lepl import List
from olive import knowledgebase

class Question(List):
    """
    A question command. It is represented by "aName".
    """
    def eval(self):
        result = knowledgebase.ask(self[0].eval())
        print result
        return result
        

class Premise(List):
    def eval(self):
        result = self[0].eval()
        knowledgebase.add(result)
        print result
        return result

