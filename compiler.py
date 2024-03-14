def compile(tokens):
    compiled = []

    for line in tokens:
        compiled.append("DEFINE NONE")

        for equality in line:
            equality = equality.strip()
            equality = equality.lower()
            equality = equality.split(" ")

            if equality[0] == "var":
                compiled.append(f"VARIABLE SET {equality[1]}")
                compiled.append(f"DEFINE VARIABLE {equality[1]}")
            elif equality[0] == "inp()":
                compiled.append("INPUT")
            elif equality[0].startswith("prt("):
                equality[0] = equality[0][4:-1] # Remove prt( and )

                compiled.append("DEFINE PRINT")

                # Textual output
                if equality[0].startswith('"'):
                    compiled.append(f"STR {equality[0].replace('"', "")}")
                # Variable output
                else:
                    compiled.append(f"VARIABLE GET {equality[0]}")

        compiled.append("DEFINE RETURN")


    return compiled
