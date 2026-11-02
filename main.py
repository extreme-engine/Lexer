def read():
    global script
    with open("codelab/test.txt", "r", encoding="utf-8") as file: script = file.read()
    print("File:\n", script, "\n")
read()

import re

def Lexer(script):
    global lex
    lex = []
    for line in re.sub(r'"""[\s\S]*?(?:"""|$)', '', script).splitlines(): #""" Multiple lines comments"""
        line = line.split('#', 1)[0] # One line comments
        tokens = line.split()   
        if tokens:lex.append(tokens)

Lexer(script)
print("Lexer:\n", lex, "\n")