from tokenizer import tokenize
from compiler import compile
from executer import execute

code = ["var hi = inp()\n", "prt(hi)\n"]

tokens = tokenize(code)
compiledCode = compile(tokens)

with open("compile.ezc", "w") as compileFile:
    for line in compiledCode:
        compileFile.write(line)
        compileFile.write("\n")

execute(compiledCode)
