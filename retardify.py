import argparse

#args
parser = argparse.ArgumentParser(description='Dedicated to speaking with idiots.')
parser.add_argument("--text", required=True, type=str, help="Pass text value you want to retardify.")

#getting args
args = parser.parse_args()
text = args.text

#yes
def retardify(text):
    lower = text.lower()
    result = ''
    for i in range(len(lower)):
        currChar = lower[i]
        if currChar.isalpha() or ' ':
            if i%2 == 1:
                result += currChar.upper()
            else:
                result += currChar
    return result

print(retardify(text))