variables = {}
returns = None
awaits = None

def execute(code):
    global returns, variables, awaits

    for line in code:

        line = line.split(" ")

        if line[0] == "VARIABLE":
            if line[1] == "SET":
                variables[line[2]] = None
            elif line[1] == "GET":
                returns = variables[line[2]]

        elif line[0] == "DEFINE":
            if line[1] == "NONE":
                awaits = None
                returns = None

            elif line[1] == "VARIABLE":
                awaits = ["VARIABLE",  line[2]]
            elif line[1] == "PRINT":
                awaits = "PRINT"

            elif line[1] == "RETURN":
                if awaits[0] == "VARIABLE":
                    variables[awaits[1]] = returns
                elif awaits == "PRINT":
                    print(returns)

        elif line[0] == "INPUT":
            returns = input()
        elif line[0] == "STR":
            returns = " ".join(line[1:])
