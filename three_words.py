def checkio(words):
    l = words.split()
    count = 0
    for i in l:
        if i.isalpha():
            count += 1
            if count > 2:
                return True
        else:
            count = 0
    return False

checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False