def checkio(data):
    fmt = "{:0>2b} {:0>4b} : {:0>3b} {:0>4b} : {:0>3b} {:0>4b}"
    ns = [int(x) for x in ''.join(n.zfill(2) for n in data.split(':'))]
    return fmt.format(*ns).replace('0', '.').replace('1', '-')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
