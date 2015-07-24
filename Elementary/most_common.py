import string
def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase,key=text.count)
print (checkio("Lorem ipsum dolor sit amet"))