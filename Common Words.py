def checkio(first, second):
    print (sorted(w for w in first.split(',') if w in second.split(',')))
    return 0

checkio("hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("x,three,one,two", "x,four,five,one,two,six,three")
