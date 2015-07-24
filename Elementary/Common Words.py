def checkio(first, second):
    return ','.join(sorted(set(first.split(',')).intersection(second.split(','))))

def checkio2(first, second):
    return (sorted(w for w in first.split(',') if w in second.split(',')))

'''
checkio("x,hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two")
'''