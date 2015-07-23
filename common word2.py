def checkio(first, second):
    return ','.join(sorted(set(first.split(',')).intersection(second.split(','))))


checkio("x,hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
print (checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two")
