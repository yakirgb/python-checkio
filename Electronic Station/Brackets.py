iparens = iter('(){}[]<>')
parens = dict(zip(iparens, iparens))
closing = parens.values()

def checkio(expression):
    stack = []
    for c in expression:
        d = parens.get(c, None)
        if d:
            stack.append(d)
        elif c in closing:
            if not stack or c != stack.pop():
                return False
    return not stack