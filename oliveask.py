import sys
from olive import grammar
from olive import knowledgebase

def eval(line):
    result = grammar.program.parse(line)[0].eval()

if __name__ == "__main__":
    user_input = sys.argv[1]
    input_file = open(user_input)
    lines = input_file.readlines()

    for line in lines:
        eval(line)
