from tokenizer import tokenize
from compiler import compile
from executer import execute

with open(input("Enter program file name (WITH EXTENSION) >>>"), "r") as file:
    code = file.readlines()

tokens = tokenize(code)
compiledCode = compile(tokens)

with open("compile.ezc", "w") as compileFile:
    for line in compiledCode:
        compileFile.write(line)
        compileFile.write("\n")

execute(compiledCode)
