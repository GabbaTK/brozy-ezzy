def tokenize(text):
    tokens = []

    for line in text:
        line = line.replace("\n", "")
        line = line.replace("==", "=")

        tokens.append(line.split("="))

    return tokens
