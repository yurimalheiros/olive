import sys
from olive import grammar
from olive import knowledgebase

def eval(line):
    result = grammar.expression.parse(line)[0].eval()
    knowledgebase.add(result)

if __name__ == "__main__":
    user_input = sys.argv[1]
    input_file = open(user_input)
    lines = input_file.readlines()

    for line in lines:
        eval(line)
